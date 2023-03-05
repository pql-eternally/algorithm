import motor

from bson import ObjectId
from mongodb import mongo_uri
from tornado.ioloop import IOLoop
from pymongo import ReadPreference

client = motor.motor_tornado.MotorClient(mongo_uri)
db = client.test


async def coro():
    collection = db.demo

    # End the session after using it.
    s = await client.start_session()
    await s.end_session()

    # Or, use an "async with" statement to end the session
    # automatically.
    async with await client.start_session() as s:
        doc = {'_id': ObjectId(), 'x': 1}
        await collection.insert_one(doc, session=s)

        secondary = collection.with_options(
            read_preference=ReadPreference.SECONDARY)

        # Sessions are causally consistent by default, so we can read
        # the doc we just inserted, even reading from a secondary.
        async for doc in secondary.find(session=s):
            print(doc)

    # Run a multi-document transaction:
    async with await client.start_session() as s:
        # Note, start_transaction doesn't require "await".
        async with s.start_transaction():
            await collection.delete_one({'x': 1}, session=s)
            await collection.insert_one({'x': 2}, session=s)

        # Exiting the "with s.start_transaction()" block while throwing an
        # exception automatically aborts the transaction, exiting the block
        # normally automatically commits it.

        # You can run additional transactions in the same session, so long as
        # you run them one at a time.
        async with s.start_transaction():
            await collection.insert_one({'x': 3}, session=s)
            await collection.update_many({'x': {'$gte': 1}},
                                         {'$inc': {'x': 1}},
                                         session=s)


IOLoop.current().run_sync(coro)
