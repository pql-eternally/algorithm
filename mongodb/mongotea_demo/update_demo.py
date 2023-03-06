import os
import sys
import unittest

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from bson import ObjectId
from mongodb.bootstrap import bootstrap_mongo
from mongodb.mixin import transactional

bootstrap_mongo()

from mongodb.globals import db, conn


class UpdateTestCase(unittest.TestCase):

    @transactional(conn)
    def test_update_doc(self, session=None):
        record = db.Account.get_from_oid('6401cba03b666a794e1b1b47')
        res = record.update_doc(doc={'name': '张三2'})
        print(res)
        record.reload()
        assert record['name'] == '张三2'

        res = record.update_doc(doc={'name': '张三3'}, check_updated_state=True)
        record.reload()
        assert record['name'] == '张三3'
        assert res is True

        age = record['age']
        doc = {
            '$inc': {
                'age': 1,
            },
        }
        record.update_doc(doc=doc, check_updated_state=True)
        record.reload()
        assert record['age'] == age + 1

    @transactional(conn)
    def test_update_set(self, session=None):
        record = db.Account.get_from_oid('6401cba03b666a794e1b1b47')
        record.update_set(set_document={'name': '张三4'})
        record.reload()
        assert record['name'] == '张三4'

        res = record.update_set(set_document={'name': '张三5'}, check_updated_state=True)
        record.reload()
        assert record['name'] == '张三5'
        assert res is True

    @transactional(conn)
    def test_update_unset(self, session=None):
        spec = {
            '_id': ObjectId('6401cba03b666a794e1b1b47'),
        }
        res = db.Account.update_unset(spec=spec, field='phone', check_updated_state=True)
        assert res is True

        spec = {}
        res = db.Account.update_unset(spec=spec, field='phone', check_updated_state=True, multi=True)
        assert res is True

    @transactional(conn)
    def test_update_inc_field(self, session=None):
        record = db.Account.get_from_oid('6401cba03b666a794e1b1b47')
        age = record['age']
        record.update_inc_field(field='age', value=1)
        record.reload()
        assert record['age'] == age + 1
        age = record['age']

        record.update_inc_field(field='age', value=-2)
        record.reload()
        assert record['age'] == age - 2

    @transactional(conn)
    def test_add_to_set(self, session=None):
        record = db.Account.get_from_oid('6401cba03b666a794e1b1b47')
        record.add_to_set(field='hobbies', value='basketball')
        record.add_to_set(field='hobbies', value=['a', 'b', 'c'], each=True)
        res = record.pull_from_set(field='hobbies', value='b')
        assert res
