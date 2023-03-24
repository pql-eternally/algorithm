import os
import sys
import motor
import pprint

_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
sys.path.append(_ROOT)

from bson import ObjectId
from tornado.ioloop import IOLoop
from mongodb import mongo_uri
from mongodb.utils import async_profile_measure

client = motor.motor_tornado.MotorClient(mongo_uri)
db = client.test


async def do_find():
    async for document in db.test.find({'i': {'$lt': 2}}):
        pprint.pprint(document)


async def do_find2():
    cursor = db.test.find({'i': {'$lt': 4}})
    # Modify the query before iterating
    cursor.sort('i', -1).skip(1).limit(2)
    async for document in cursor:
        pprint.pprint(document)


@async_profile_measure()
async def do_motor_find():
    record = await db.account.find_one({'_id': ObjectId('641d013c52ecce87f5ecd0f5')})
    # operator_info = record.operator_info
    print(record)


@async_profile_measure()
async def do_motor_multi_find():
    async for record in db.account.find({}):
        record = await db.account.find_one({'_id': record['_id']})
        # operator_info = record.operator_info


# IOLoop.current().run_sync(do_find)
# IOLoop.current().run_sync(do_motor_find)
IOLoop.current().run_sync(do_motor_multi_find)
