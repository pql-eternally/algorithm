import os
import sys
import unittest

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from mongodb.mixin import transactional
from mongodb.bootstrap import bootstrap_mongo

bootstrap_mongo()

from mongodb.globals import db, conn


class LockTestCase(unittest.TestCase):

    @transactional(conn)
    def test_lock(self, session=None):
        record = db.Account.get_from_oid('64054dfaa265fbda3e4d1ede')
        record.lock_with_retry()
        assert record
