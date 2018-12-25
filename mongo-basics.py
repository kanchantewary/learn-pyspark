#run basic mongo commands from python

import pymongo
from pymongo import MongoClient

#lazy evaluation. defines connection to mongodb in localhost
client = MongoClient('localhost')

#lazy evaluation, define database
db = client.packt

#creates the collection (db is created in this step as well)
testCollection = db.testCollection

#insert a document(row)
testCollection.insert_one({'a':1})

#find one row
print(testCollection.find_one())

#expected to print all rows, but only prints the object id
print(testCollection.find())

#print the count
print(testCollection.count())

#drop the collection(table)
#db.drop_collection('testCollection')

#drop the database
#client.drop_database('packt')

#find all values using a cursor
cur=db.testCollection.find()
for doc in cur:
    print(doc)

#embedded documents

embedded=db.embedded

#insert a document with nested array

embedded.insert_one({'ages':[34,45,29,67]})
embedded.insert_one({'ages':[23,78,12,76]})

#LEARNING: find(query, projection) --query is the condition to match, projection is the fields to return

#find one matching document, projection operator is 'id=0'
print(embedded.find_one({'ages':[34,45,29,67]},{'_id':0}))

#match on presence of element in an array
print(embedded.find_one({'ages':30},{'_id':0}))

#Match array with conditions on any element in array
print(embedded.find_one({'ages':{'$gt':30,'$lt':20}},{'_id':0}))

#match array with conditions on any single element of array
print(embedded.find_one({'ages':30},{'_id':0}))

#match by array index
#embedded.find_one({'ages':{$elemMatch:{'$gt:30,'$lt':20}},{'_id'=0})
#match by condition on array index




