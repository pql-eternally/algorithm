import arrow
import pandas as pd
import fire

from pymongo import MongoClient
from yoda import datetime as datetime_utils

client = MongoClient('192.168.10.134', 27003)
db = client['aoao-plus']


class OrderLoader(object):
    def export_city_order(self, city_code):
        """
        导出北京市订单数据
        """
        data = []

        # 按城市读取订单数据
        spec = {
            "shipping_date": {"$gte": 20230801, "$lte": 20230901},
            "city_code": city_code,
            "state": {"$in": [100]},
        }
        records = list(db['order.vendor_order'].find(spec))
        for record in records:
            delivery_info = record['delivery_info']
            row = {
                'shipping_date': record['shipping_date'],  # 配送日期
                'order_id': record['_id'],  # 订单ID
                'state': record['state'],
                'operator_id': record['operator_id'],  # 用户ID
                'is_timeout': record['is_timeout'],  # 是否超时
                'created_at': datetime_utils.to_prc(record['created_at']),  # 下单时间
                'confirmed_at': datetime_utils.to_prc(record['confirmed_at']),  # 确认时间
                'accepted_at': datetime_utils.to_prc(delivery_info['accepted_at']),  # 接单时间
                'arrived_at': datetime_utils.to_prc(delivery_info['arrived_at']),  # 到店时间
                'pickup_at': datetime_utils.to_prc(delivery_info['pickup_at']),  # 取货时间
                'done_at': datetime_utils.to_prc(delivery_info['done_at']),  # 送达时间
            }
            data.append(row)
        df = pd.DataFrame(data)
        print(f'Total count: {df.index.size}')
        df.to_csv(f'8月<{city_code}>订单.csv', index=False)


if __name__ == '__main__':
    fire.Fire(OrderLoader)
