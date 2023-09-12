import fire
import pandas as pd

from pymongo import MongoClient
from yoda import datetime as datetime_utils

client = MongoClient('192.168.10.134', 27003)
db = client['aoao-plus']
qcode_db = client['boss-qcode']


class OrderLoader(object):

    @property
    def city_map(self):
        """
        加载城市映射表
        """
        city_map = {}
        records = qcode_db['qcode.biz_meta.city'].find()
        for record in records:
            city_map[record['_id']] = record['city_name']
        return city_map

    @property
    def store_map(self):
        """
        加载门店映射表
        """
        store_map = {}
        records = db['seller.store'].find()
        for record in records:
            store_map[record['_id']] = record['name']
        return store_map

    @property
    def account_map(self):
        """
        加载用户映射表
        """
        account_map = {}
        records = db['account'].find()
        for record in records:
            account_map[record['_id']] = record['name']
        return account_map

    def export_city_order(self, city_code=None, start_date=None, end_date=None):
        """
        按城市导出订单数据
        """

        def _process_records(records):
            for record in records:
                seller_order_id = record['seller_order_id']
                seller_order_record = db['order.seller_order'].find_one({'_id': seller_order_id})
                if not seller_order_record:
                    continue
                delivery_info = record['delivery_info']
                store_id = record['store_id']
                operator_id = record['operator_id']
                row = {
                    'shipping_date': record['shipping_date'],  # 配送日期
                    'city_code': record['city_code'],
                    'city_name': city_name,
                    'store_id': store_id,  # 门店ID
                    'store_name': self.store_map.get(store_id),  # 门店名称
                    'operator_id': operator_id,  # 用户ID
                    'operator_name': self.account_map.get(operator_id),  # 用户姓名
                    'order_id': record['_id'],  # 订单ID
                    'seller_order_id': seller_order_id,  # 商家订单ID
                    'distance': seller_order_record['distance'],  # 配送距离
                    'consignee_poi': seller_order_record['consignee_info']['poi'],  # 收货地址坐标
                    'consignor_poi': seller_order_record['consignor_info']['poi'],  # 发货地址坐标
                    'state': record['state'],
                    'is_timeout': record['is_timeout'],  # 是否超时
                    'created_at': datetime_utils.to_prc(record['created_at']),  # 下单时间
                    'confirmed_at': datetime_utils.to_prc(record['confirmed_at']),  # 确认时间
                    'accepted_at': datetime_utils.to_prc(delivery_info['accepted_at']),  # 接单时间
                    'arrived_at': datetime_utils.to_prc(delivery_info['arrived_at']),  # 到店时间
                    'pickup_at': datetime_utils.to_prc(delivery_info['pickup_at']),  # 取货时间
                    'done_at': datetime_utils.to_prc(delivery_info['done_at']),  # 送达时间
                }
                yield row

        spec = {
            "state": {"$in": [100]},
        }
        if city_code:
            city_code = str(city_code)
            spec['city_code'] = str(city_code)
            city_name = self.city_map.get(city_code)
        else:
            city_name = '全部城市'

        # 按配送日期过滤
        if start_date or end_date:
            spec['shipping_date'] = {}
            if start_date:
                spec['shipping_date']['$gte'] = start_date
            if end_date:
                spec['shipping_date']['$lte'] = end_date
        records = db['order.vendor_order'].find(spec)
        df = pd.DataFrame(_process_records(records))
        count = df.index.size
        if count == 0:
            print('No records found.')
            return
        file_path = f'../data/{city_name}<{start_date}-{end_date}>订单.csv'
        df.to_csv(file_path, index=False)
        print(f'Total {df.index.size} records exported to {file_path} done.')


if __name__ == '__main__':
    fire.Fire(OrderLoader)
