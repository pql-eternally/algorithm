import fire
import os
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from bson import ObjectId
from mongodb.bootstrap import bootstrap_mongo

bootstrap_mongo()

from mongodb.globals import db
from mongodb.utils import profile_measure


class PyMongoCli:

    @profile_measure()
    def do_find(self):
        record = db.account.find_one({'_id': ObjectId('641d013c52ecce87f5ecd0f5')})
        print(record)

    @profile_measure()
    def do_multi_find(self):
        records = db.account.find()
        print(records.count())
        for record in records:
            record = db.account.find_one({'_id': record['_id']})

    @profile_measure()
    def do_mongotea_find(self):
        record = db.Account.get_from_oid('641d013c52ecce87f5ecd0f5')
        # operator_info = record.operator_info
        print(record)

    @profile_measure()
    def do_mongotea_multi_find(self):
        records = db.Account.find().limit(50)
        print(records.count())
        for record in records:
            record = db.Account.get_from_oid(record['_id'])
            franchisee_info = record.franchisee_info
            operator_info = record.operator_info

    def do_mongotea_all_find(self, limit: int = 10):
        spec = {
            'operator_id': {
                '$exists': True,
                '$ne': None,
            },
            'franchisee_id': {
                '$exists': True,
                '$ne': None,
            },
        }
        records = list(db.Account.find(spec).limit(limit))

        @profile_measure()
        def f1():
            for record in records:
                record = db.Account.get_from_oid(record['_id'])

        @profile_measure()
        def f2():
            for record in records:
                record = db.Account.get_from_oid(record['_id'])
                franchisee_info = record.franchisee_info

        @profile_measure()
        def f3():
            for record in records:
                record = db.Account.get_from_oid(record['_id'])
                franchisee_info = record.franchisee_info
                operator_info = record.operator_info

        f1()
        print('===' * 30)
        f2()
        print('===' * 30)
        f3()


if __name__ == '__main__':
    fire.Fire(PyMongoCli)
