
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = uri = "mongodb+srv://mrmanishsingh3005_db_user:Admin%40123@cluster0.bq7qtgj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)