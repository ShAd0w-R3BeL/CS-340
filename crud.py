from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, PyMongoError

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        """
        Initializes the MongoClient to connect to the authenticated 
        MongoDB instance using the provided user credentials.
        """
        USER = username
        PASS = password
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        
        try:
            # Authenticating against 'admin' where the user is created
            self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}/?authSource=admin')
            self.database = self.client[DB]
            self.collection = self.database[COL]
            
            # Direct ping test to force authentication validation immediately
            self.client.admin.command('ping')
            print("Successfully connected to the MongoDB 'aac' database.")
        except (ConnectionFailure, PyMongoError) as e:
            print(f"Database connection failed: {e}")
            raise

    def create(self, data):
        """ Inserts a document into the specified MongoDB collection. """
        if data is not None and isinstance(data, dict) and len(data) > 0:
            try:
                self.collection.insert_one(data)
                return True
            except PyMongoError as e:
                print(f"An error occurred during insertion: {e}")
                return False
        else:
            print("Insertion failed: Material to insert must be a valid, non-empty dictionary.")
            return False

    def read(self, query=None):
        """ Queries for documents from the specified MongoDB collection. """
        if query is None:
            query = {}
        elif not isinstance(query, dict):
            print("Query failed: Search parameter must be a dictionary data type.")
            return []

        try:
            cursor = self.collection.find(query)
            return list(cursor)
        except PyMongoError as e:
            print(f"An error occurred during query execution: {e}")
            return []
        
    def update(self, query, new_data):
        """
        Updates documents in the collection that match the query.
        Input: query (dict), new_data (dict)
        Return: The number of objects modified.
        """
        if query is not None and new_data is not None:
            try:
                # Use update_many to update all matching documents
                result = self.collection.update_many(query, {"$set": new_data})
                return result.modified_count
            except PyMongoError as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            print("Update failed: Query or data parameter is empty.")
            return 0

    def delete(self, query):
        """
        Deletes documents from the collection that match the query.
        Input: query (dict)
        Return: The number of objects removed.
        """
        if query is not None:
            try:
                # Use delete_many to remove all matching documents
                result = self.collection.delete_many(query)
                return result.deleted_count
            except PyMongoError as e:
                print(f"An error occurred during deletion: {e}")
                return 0
        else:
            print("Delete failed: Query parameter is empty.")
            return 0