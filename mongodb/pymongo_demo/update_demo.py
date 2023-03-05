import fire
import os
import sys
import time

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from bson import ObjectId
from pymongo import UpdateOne, UpdateMany
from mongodb.mixin import transactional
from mongodb.bootstrap import bootstrap_mongo
from mongodb.utils import monitor_exception

bootstrap_mongo()

from mongodb.globals import db, conn


class PyMongoCli:

    @transactional(conn)
    def do_update_transaction(self, session):
        t = int(time.time())
        res1 = db.account.update_one(
            {"_id": ObjectId("63ff0be27ee88ad9fdb5fdea")},
            {"$set": {"name": f"李四{t}"}},
            session=session
        )
        print(f"res1 update ok: {res1.raw_result['ok']}")

        monitor_exception()

        res2 = db.account.update_one(
            {"_id": ObjectId("63ff0be27ee88ad9fdb5fde9")},
            {"$set": {"name": f"张三{t}"}},
            session=session
        )
        print(f"res2 update ok: {res2.raw_result['ok']}")

    @transactional(conn)
    def do_update_multi_collection(self, session):
        t = int(time.time())
        res1 = db.staff.update_one(
            {"_id": ObjectId("640005c3cdc1f3d3989768a9")},
            {"$set": {"name": f"张三{t}"}},
            session=session
        )
        print(f"res1 update ok: {res1.raw_result['ok']}")

        monitor_exception()

        res2 = db.employee.update_one(
            {"_id": ObjectId("640005c3cdc1f3d3989768aa")},
            {"$set": {"name": f"李四{t}"}},
            session=session
        )
        print(f"res2 update ok: {res2.raw_result['ok']}")

    @transactional(conn)
    def do_multi_update(self, session):
        requests = [
            UpdateOne({"_id": ObjectId("63ff0be27ee88ad9fdb5fdea")}, {'$set': {'do_multi_update': time.time()}}),
            UpdateOne({"_id": ObjectId("63ff0be27ee88ad9fdb5fde9")}, {'$set': {'do_multi_update': time.time()}}),
        ]
        res = db.account.bulk_write(requests, session=session)
        print(res)

    @transactional(conn)
    def do_update_many(self, session):
        requests = [
            UpdateOne({"_id": ObjectId("63ff0be27ee88ad9fdb5fdea")}, {'$set': {'do_update_many': time.time()}}),
            UpdateOne({"_id": ObjectId("63ff0be27ee88ad9fdb5fde9")}, {'$set': {'do_update_many': time.time()}}),
            UpdateMany({'name': '李四'}, {'$set': {'do_update_many': time.time()}}),
        ]
        res = db.account.bulk_write(requests, session=session)
        print(res)


if __name__ == '__main__':
    fire.Fire(PyMongoCli)
