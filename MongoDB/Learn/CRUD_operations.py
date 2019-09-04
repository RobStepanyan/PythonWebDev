# CRUD operations create, read, update, and delete documents.
import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['CRUD']

"""
1. Insert Documents

This section provides examples of insert operations in MongoDB.

CREATING A COLLECTION
If the collection does not currently exist, insert operations will create the collection.
"""

# Insert a Single Document
db.inventory.insert_one(
    {
        'item': 'canvas',
        'qty': 100,
        'tags': ['cotton'],
        'size': {
            'h': 28, 'w': 35.5, 'uom': 'cm'
        }
    }
)

# To retrieve the document that you just inserted, query the collection:
cursor = db.inventory.find({'item': 'canvas'})

# Insert Multiple Documents
db.inventory.insert_many([
    {
        "item": "journal",
        "qty": 25,
        "tags": ["blank", "red"],
        "size": {
            "h": 14, "w": 21, "uom": "cm"
        }
    },
    {
        "item": "mat",
        "qty": 85,
        "tags": ["gray"],
        "size": {
            "h": 27.9, "w": 35.5, "uom": "cm"
        }
    },
    {
        "item": "mousepad",
        "qty": 25,
        "tags": ["gel", "blue"],
        "size": {
            "h": 19, "w": 22.85, "uom": "cm"
        }
    }
])

# To retrieve the inserted documents, query the collection:
cursor = db.inventory.find({})

print(cursor)
# <pymongo.cursor.Cursor object at 0x0000021CDBF34D48>
print(cursor[0])
# {'_id': ObjectId('5d6e9c24853a5739cc5db5bd'), 'item': 'canvas', 'qty': 100,
# 'tags': ['cotton'], 'size': {'h': 28, 'w': 35.5, 'uom': 'cm'}}


"""
Query Documents

This section provides examples of query operations using the pymongo.collection.Collection.find() method 
in the PyMongo Python driver. The examples on this page use the inventory collection. 
To populate the inventory collection, run the following:
"""
db.inventory.insert_many([
    {"item": "journal",
     "qty": 25,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "notebook",
     "qty": 50,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "A"},
    {"item": "paper",
     "qty": 100,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "D"},
    {"item": "planner",
     "qty": 75, "size": {"h": 22.85, "w": 30, "uom": "cm"},
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": {"h": 10, "w": 15.25, "uom": "cm"},
     "status": "A"}])

# Select All Documents in a Collection
cursor = db.inventory.find({})

# Specify Equality Condition
cursor = db.inventory.find({'status': 'A'})
print(cursor)
# {'_id': ObjectId('5d6e9c24853a5739cc5db5bd'), 'item': 'canvas', 'qty': 100,
# 'tags': ['cotton'], 'size': {'h': 28, 'w': 35.5, 'uom': 'cm'}}

# Specify Conditions Using Query Operators
cursor = db.inventory.find({'status': {'$in': ['A', 'D']}})

# Specify AND Conditions
cursor = db.inventory.find({'status': 'A', 'qty': {'$lt': 30}})

# Specify OR Conditions
cursor = db.inventory.find(
    {'$or': [{'status': 'A'}, {'qty': {'$lt': 30}}]}
)

# Specify AND as well as OR Conditions
cursor = db.inventory.find(
    {'status': 'A', '$or': [{'qty': {'$lt': 30}}, {'item': {'$regex': '^p'}}]}
)


"""
Update Documents

The examples on this section use the inventory collection. 
"""

# Update a Single Document
db.inventory.update_one(
    {'item': 'paper'},
    {
        '$set': {'size.uom': 'cm', 'status': 'P'},
        '$currentDate': {'lastModified': True}
    }
)

# Update Multiple Documents
db.inventory.update_many(
    {'qty': {'$lt': 50}},
    {
        '$set': {'size.uom': 'in', 'status': 'P'},
        '$currentDate': {'lastModified': True}
    }
)

# Replace a Document
db.inventory.replace_one(
    {'item': 'paper'},
    {
        'item': 'paper',
        'instock': [
                {'warehouse': 'A', 'qty': 60},
                {'warehouse': 'B', 'qty': 40}
        ]
    }
)


"""
Delete Documents

The examples on this page use the inventory collection.
"""

# Delete All Documents that Match a Condition
db.inventory.delete_many(
    {'status': 'A'}
)

# Delete Only One Document that Matches a Condition
db.inventory.delete_one(
    {'status': 'D'}
)

# Delete All Docuements
db.invnetory.delete_many({})
