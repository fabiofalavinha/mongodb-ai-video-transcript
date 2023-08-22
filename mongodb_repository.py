from pymongo import MongoClient


class MongoDbRepository:
    def __init__(self, connection_string: str, database: str, collection: str):
        self.client = MongoClient(connection_string)
        self.database = self.client[database]
        self.collection = self.database[collection]

    def insertOne(self, data):
        return self.collection.insert_one(data).inserted_id

    def updateOne(self, filter_condition, update_data):
        return self.collection.update_one(filter_condition, {'$set': update_data})

    def findById(self, _id):
        return self.collection.find_one({"_id": _id})

    def storeEmbedding(self, video_id, embedding):
        return self.collection.update_one({"_id": video_id}, {'$set': {"embedding": embedding}})

    def searchBy(self, text: str):
        return self.collection.find({"$search": text})
