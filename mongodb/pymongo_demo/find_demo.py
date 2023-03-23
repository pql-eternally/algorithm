import fire
import os
import sys

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from mongodb.bootstrap import bootstrap_mongo

bootstrap_mongo()

from mongodb.globals import db
from mongodb.utils import profile_measure
print(db)

class PyMongoCli:

    @profile_measure()
    def do_find(self):
        records = db.account.find({})
        print(records.count())

    @profile_measure()
    def do_mongotea_find(self):
        records = db.Account.find({})
        print(records.count())


if __name__ == '__main__':
    fire.Fire(PyMongoCli)
