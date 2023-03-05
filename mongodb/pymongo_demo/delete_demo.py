import fire
import os
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from pymongo import DeleteOne, DeleteMany
from mongodb.utils import monitor_exception
from mongodb.mixin import transactional
from mongodb.bootstrap import bootstrap_mongo
from yoda import convert

bootstrap_mongo()

from mongodb.globals import db, conn


class PyMongoCli:

    @transactional(conn)
    def do_remove_transaction(self, session):
        res1 = db.account.delete_one(
            {"_id": convert.to_object_id("640190f0bc5c14cc4e7bd688")},
            session=session
        )
        print(f"res1 delete ok: {res1.raw_result['ok']}")

        monitor_exception()

        res2 = db.account.delete_one(
            {"_id": convert.to_object_id("64000aef736738625094c208")},
            session=session
        )
        print(f"res2 delete ok: {res2.raw_result['ok']}")

    @transactional(conn)
    def do_multi_remove(self, session):
        requests = [
            DeleteOne({"name": "delete_one1"}),
            DeleteOne({"name": "delete_one2"}),
            DeleteMany({"name": "delete_many"}),
        ]
        res = db.account.bulk_write(requests, session=session)
        print(res.bulk_api_result)


if __name__ == '__main__':
    fire.Fire(PyMongoCli)
