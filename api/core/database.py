import pymongo
from api.config.settings import settings

client = pymongo.MongoClient(settings.mongo_db_connection_uri)