__author__ = 'vcoder'
import pymongo
from pymongo import MongoClient

client = MongoClient()

client = MongoClient('localhost', 27017)

db = client['test-database']
