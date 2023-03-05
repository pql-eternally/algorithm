import motor

from mongodb import mongo_uri
from tornado.ioloop import IOLoop

client = motor.motor_tornado.MotorClient(mongo_uri)
db = client.test


async def do_insert():
    result = await db.test.insert_many([{'i': i} for i in range(2000)])
    print('inserted %d docs' % (len(result.inserted_ids),))


IOLoop.current().run_sync(do_insert)
