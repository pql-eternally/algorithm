import fire
import os
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from pymongo import InsertOne
from mongodb.mixin import transactional
from mongodb.bootstrap import bootstrap_mongo
from mongodb.utils import monitor_exception

bootstrap_mongo()

from mongodb.globals import db, conn


class PyMongoCli:

    @transactional(conn)
    def do_insert_transaction(self, session):
        res1 = db.account.insert_one({"name": "张三", "age": 18}, session=session)
        print(res1.inserted_id)

        monitor_exception()

        res2 = db.account.insert_one({"name": "李四", "age": 20}, session=session)
        print(res2.inserted_id)

    @transactional(conn)
    def do_insert_multi_collection(self, session):
        res1 = db.staff.insert_one({"name": "张三2", "age": 18}, session=session)
        print(res1.inserted_id)

        monitor_exception()

        res2 = db.employee.insert_one({"name": "李四", "age": 20}, session=session)
        print(res2.inserted_id)

    @transactional(conn)
    def do_multi_insert(self, session):
        requests = [
            InsertOne({"name": "do_multi_insert1", "age": 18}),
            InsertOne({"name": "do_multi_insert2", "age": 20}),
            InsertOne({"name": "delete_one1"}),
            InsertOne({"name": "delete_one2"}),
            InsertOne({"name": "delete_many"}),
            InsertOne({"name": "delete_many"}),
        ]
        res = db.account.bulk_write(requests, session=session)
        print(res)


if __name__ == '__main__':
    fire.Fire(PyMongoCli)
