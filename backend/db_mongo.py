import database

import pymongo
from pymongo import MongoClient
import copy

class Database(database.Database):

	def __init__(self):
		database.Database.__init__(self)
		client = None
		db = None
		collection = None
		recent = None

		host = 'localhost'
		port = 27017
		timeout = 20
		database_name = 'radiowcs'
		authkey = ''
		table_name = 'playlist'
		table_recent = 'recent'

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		if (connection != None):
			connection.close()

	def connect(self):
		"""Return db and client"""
		client = MongoClient(self.host ,self.port)
		db = client[self.database_name]
		collection = db[self.table_name]
		recent = db[self.table_recent]
		return db, collection

	def configure(self):
		""" Not needed for mongodb"""
		pass

	def insert(item):
		"""Insert into database"""
		new_item = copy.deepcopy(item)
		collection.insert(new_item)
		recent.insert()

