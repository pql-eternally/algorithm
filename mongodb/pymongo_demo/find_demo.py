import fire
import os
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from mongodb.bootstrap import bootstrap_mongo

bootstrap_mongo()

from mongodb.globals import db
from mongodb.utils import profile_measure


class PyMongoCli:

    @profile_measure()
    def do_find(self):
        record = db.account.find_one({'_id': '6405913d8d03ebec148a9746'})
        print(record)

    @profile_measure()
    def do_mongotea_find(self):
        record = db.Account.get_from_oid('6405913d8d03ebec148a9746')
        # operator_info = record.operator_info
        print(record)


if __name__ == '__main__':
    fire.Fire(PyMongoCli)
