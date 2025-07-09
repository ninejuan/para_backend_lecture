import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

client = pymongo.MongoClient(os.getenv('DB_URI'))
db = client[os.getenv('DB_NAME')] # == Collection