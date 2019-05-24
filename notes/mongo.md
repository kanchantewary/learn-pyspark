# Learn the basics of MongoDB

https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/
https://docs.mongodb.com/manual/mongo/

https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb

start mongo service
sudo service mongod start
stop mongo service
sudo service mongod stop
restart mongo service
sudo service mongod restart

Repo to watch out:
https://github.com/ghaughian/mongo-kafka-spark

select all records(documents) from a table(collection)
db.collection.find() 

Use db.collection.insertOne() to insert a single document.

db.inventory.find( { status: "D" } )
