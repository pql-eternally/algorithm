import motor
import pprint

from mongodb import mongo_uri
from tornado.ioloop import IOLoop

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


# IOLoop.current().run_sync(do_find)
IOLoop.current().run_sync(do_find2)
