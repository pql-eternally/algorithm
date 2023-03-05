import motor

from mongodb import mongo_uri
from tornado.ioloop import IOLoop

client = motor.motor_tornado.MotorClient(mongo_uri)
db = client.test


async def do_count():
    n = await db.test.count_documents({})
    print('%s documents in collection' % n)
    n = await db.test.count_documents({'i': {'$gt': 1000}})
    print('%s documents where i > 1000' % n)


IOLoop.current().run_sync(do_count)
