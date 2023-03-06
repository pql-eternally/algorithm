import fire
import os
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
        record = db.Account()
        doc = {
            'name': '王五',
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
