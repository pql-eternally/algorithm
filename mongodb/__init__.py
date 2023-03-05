from pymongo import MongoClient

# mongo_uri = 'mongodb://127.0.0.1:27017,127.0.0.1:27018,127.0.0.1:27019'
mongo_uri = 'mongodb://192.168.10.134:27003,192.168.10.134:27004,192.168.10.134:27005'

# Create a client
client = MongoClient(mongo_uri)
