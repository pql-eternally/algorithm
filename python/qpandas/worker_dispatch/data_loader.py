import os
import fire
import pandas as pd

from pymongo import MongoClient
from yoda import datetime as datetime_utils

# FIXME: 修改为线上数据库
client = MongoClient('192.168.10.134', 27003)
db = client['aoao-plus']
qcode_db = client['boss-qcode']


class DataLoader(object):

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

    def export_city_order(self, start_date=None, end_date=None, city_code=None, city_name=None, file_path='/tmp'):
        """
        按城市导出订单数据
        包含字段：
            shipping_date: 配送日期
            city_code: 城市编码
            city_name: 城市名称
            store_id: 门店ID
            store_name: 门店名称
            operator_id: 用户ID
            operator_name: 用户姓名
            order_id: 订单ID
            seller_order_id: 商家订单ID
            distance: 配送距离
            consignee_poi_lon: 收货地址经度
            consignee_poi_lat: 收货地址纬度
            consignor_poi_lon: 发货地址经度
            consignor_poi_lat: 发货地址纬度
            state: 订单状态
            is_timeout: 是否超时
            created_at: 下单时间
            confirmed_at: 确认时间
            accepted_at: 接单时间
            arrived_at: 到店时间
            pickup_at: 取货时间
            done_at: 送达时间
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

                try:
                    consignee_poi_lon, consignee_poi_lat = seller_order_record['consignee_info']['poi']
                except ValueError:
                    consignee_poi_lon, consignee_poi_lat = 0, 0
                try:
                    consignor_poi_lon, consignor_poi_lat = seller_order_record['consignor_info']['poi']
                except ValueError:
                    consignor_poi_lon, consignor_poi_lat = 0, 0

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
                    'consignee_poi_lon': consignee_poi_lon,  # 收货地址经度
                    'consignee_poi_lat': consignee_poi_lat,  # 收货地址纬度
                    'consignor_poi_lon': consignor_poi_lon,  # 发货地址经度
                    'consignor_poi_lat': consignor_poi_lat,  # 发货地址纬度
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
            spec['city_code'] = city_code
            city_name = self.city_map.get(city_code)
        elif city_name:
            spec['city_name'] = city_name
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
        current_day = datetime_utils.prcnow().format('YYYYMMDD')
        file_name = f'{city_name}-{end_date or current_day}-订单.csv'
        file_path = os.path.join(file_path, file_name)
        df.to_csv(file_path, index=False)
        print(f'Total {df.index.size} order records exported to {file_path} done.')

    def export_store(self, file_path='/tmp'):
        """
        导出门店数据，包含门店 ID、名称、坐标、创建时间
        """

        def _process_records(records):
            for record in records:
                try:
                    lon, lat = record['poi']
                except ValueError:
                    lon, lat = None, None

                row = {
                    'store_id': record['_id'],
                    'store_name': record['name'],
                    'store_poi_lon': lon,
                    'store_poi_lat': lat,
                    'created_at': datetime_utils.to_prc(record['created_at']),
                }
                yield row

        spec = {}
        records = db['seller.store'].find(spec)
        df = pd.DataFrame(_process_records(records))
        count = df.index.size
        if count == 0:
            print('No records found.')
            return
        file_name = '门店.csv'
        file_path = os.path.join(file_path, file_name)
        df.to_csv(file_path, index=False)
        print(f'Total {df.index.size} store records exported to {file_path} done.')


if __name__ == '__main__':
    fire.Fire(DataLoader)
