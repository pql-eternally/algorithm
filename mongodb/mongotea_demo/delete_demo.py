import os
import sys
import unittest

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from bson import ObjectId
from mongodb.bootstrap import bootstrap_mongo

bootstrap_mongo()

from mongodb.globals import db


class FindTestCase(unittest.TestCase):

    def test_remove_by_id(self):
        res = db.Account.remove_by_id(ObjectId('6405773192d015c14f20aa13'))
        print(res)
        assert res

        res = db.Account.collection.remove({'_id': ObjectId('6405773192d015c14f20aa13')})
        assert res

    def test_remove_by_oid(self):
        res = db.Account.remove_by_oid('6405773192d015c14f20aa13')
        print(res)
        assert res
