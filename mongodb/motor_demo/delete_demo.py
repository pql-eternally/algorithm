import motor
import pprint

from mongodb import mongo_uri
from tornado.ioloop import IOLoop

client = motor.motor_tornado.MotorClient(mongo_uri)
db = client.test


async def do_delete_one():
    n = await db.test.count_documents({})
    pprint.pprint('%s documents before calling delete_one()' % n)
    result = await db.test.delete_one({'i': {'$gte': 1000}})
    pprint.pprint('%s documents after' % (await db.test.count_documents({})))


IOLoop.current().run_sync(do_delete_one)
