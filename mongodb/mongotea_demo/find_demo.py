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

    def test_find_one(self):
        record = db.Account.find_one({'name': '张三'})
        print(record)

    def test_get_from_oid(self):
        record = db.Account.get_from_oid('6401cbe0f413cd95e8834a9b')
        assert record['_id'] == ObjectId('6401cbe0f413cd95e8834a9b')

    def test_find(self):
        spec = {
            'name': '张三',
        }
        records = db.Account.find(spec)
        print(records)
        cnt = records.count()
        print(cnt)
