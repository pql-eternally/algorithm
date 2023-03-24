import os
import random
import sys
import unittest

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from mongodb.utils import monitor_exception
from mongodb.mixin import transactional
from mongodb.bootstrap import bootstrap_mongo

bootstrap_mongo()

from mongodb.globals import db, conn


class InsertTestCase(unittest.TestCase):

    @transactional(conn)
    def test_insert(self, session):
        account_ids = [record['_id'] for record in db.Account.find({})]
        franchisee_ids = [record['_id'] for record in db.Franchisee.find({})]

        for i in range(100):
            record = db.Account()
            doc = {
                'name': str(random.random()),
                'age': random.randint(1, 100),
                'franchisee_id': random.choice(franchisee_ids),
                'creator_id': random.choice(account_ids),
                'operator_id': random.choice(account_ids),
            }
            record.update(doc)
            record.insert(session=session)

    @transactional(conn)
    def test_save(self, session):
        record = db.Account()
        record['name'] = '张三'
        record.save(session=session)
        print(record)

        record = db.Account()
        record['name'] = '李四'
        record.save(session=session)
        monitor_exception()

    @transactional(conn)
    def do_insert_multi_collection(self, session):
        # pymongo.errors.OperationFailure: Cannot create namespace test.staff in multi-document transaction.
        # Create a new collection outside of a transaction
        # db.create_collection(db.Staff.__collection__)
        # db.create_collection(db.Employee.__collection__)

        record = db.Staff()
        record['name'] = '张三'
        record.save(session=session)

        record = db.Employee()
        record['name'] = '李四'
        record.save(session=session)
        monitor_exception()

    def test_apply_form_save(self):
        record = db.Account()
        form_data = {
            'name': '张三',
            'age': 18,
        }
        record.apply_form_save(form=form_data)
        print(record)
        assert record

    def test_apply_form_update_set(self):
        record = db.Account.get_from_oid('6405774e50d433b679b7952f')
        form_data = {
            'name': '李四',
        }
        record.apply_form_update_set(form_data)
        record.reload()
        assert record['name'] == '李四'
