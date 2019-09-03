import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mongo_practice']

# Listing all local databases
# Important: In MongoDB, a database is not created until it gets content!
print(client.list_database_names())  # ['admin', 'config', 'local']

# Insert Into Collection
coll = db['Collection1']
coll.insert_one({"name": "John", "address": "Highway 37"})
# ['admin', 'config', 'local', 'mongo_practice']
print(client.list_database_names())
print(db.list_collection_names())  # ['Collection1']

# Insert Multiple Documents Into Collection
list_of_dict = [
    {"name": "Amy", "address": "Apple st 652"},
    {"name": "Hannah", "address": "Mountain 21"},
    {"name": "Michael", "address": "Valley 345"},
    {"name": "Sandy", "address": "Ocean blvd 2"},
    {"name": "Betty", "address": "Green Grass 1"},
    {"name": "Richard", "address": "Sky st 331"},
    {"name": "Susan", "address": "One way 98"},
    {"name": "Vicky", "address": "Yellow Garden 2"},
    {"name": "Ben", "address": "Park Lane 38"},
    {"name": "William", "address": "Central st 954"},
    {"name": "Chuck", "address": "Main Road 989"},
    {"name": "Viola", "address": "Sideway 1633"}
]
x = coll.insert_many(list_of_dict)
# [ObjectId('5d68b502e00fb4f32623a1ee'), ObjectId('5d68b502e00fb4f32623a1ef')....
print(x.inserted_ids)

# Insert Multiple Documents, with Specified IDs
coll = db['Collection2']
list_of_dict = [
    {"_id": 1, "name": "John", "address": "Highway 37"},
    {"_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    {"_id": 3, "name": "Amy", "address": "Apple st 652"},
    {"_id": 4, "name": "Hannah", "address": "Mountain 21"},
    {"_id": 5, "name": "Michael", "address": "Valley 345"},
    {"_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    {"_id": 7, "name": "Betty", "address": "Green Grass 1"},
    {"_id": 8, "name": "Richard", "address": "Sky st 331"},
    {"_id": 9, "name": "Susan", "address": "One way 98"},
    {"_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    {"_id": 11, "name": "Ben", "address": "Park Lane 38"},
    {"_id": 12, "name": "William", "address": "Central st 954"},
    {"_id": 13, "name": "Chuck", "address": "Main Road 989"},
    {"_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
# coll.insert_many(list_of_dict)
print(x.inserted_ids)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# Find One
# To select data from a collection in MongoDB, we can use the find_one() method.
# The find_one() method returns the first occurrence in the selection.
print(coll.find_one())  # {'_id': 1, 'name': 'John', 'address': 'Highway 37'}

# Find All
# To select data from a table in MongoDB, we can also use the find() method.
# The find() method returns all occurrences in the selection.
# The first parameter of the find() method is a query object. In this example we use an empty query object, which selects all documents in the collection.
# No parameters in the find() method gives you the same result as SELECT * in MySQL.
for d in coll.find():
    print(d)

# {'_id': 1, 'name': 'John', 'address': 'Highway 37'}
# {'_id': 1, 'name': 'John', 'address': 'Highway 37'}
# {'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
# ..........
