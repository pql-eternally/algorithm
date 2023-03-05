import motor
import pprint

from mongodb import mongo_uri
from tornado.ioloop import IOLoop

client = motor.motor_tornado.MotorClient(mongo_uri)
db = client.test


async def do_update():
    result = await db.test.update_one({'i': 51}, {'$set': {'key': 'value'}})
    print('updated %s document' % result.modified_count)
    new_document = await db.test.find_one({'i': 51})
    print('document is now %s' % pprint.pformat(new_document))


IOLoop.current().run_sync(do_update)
