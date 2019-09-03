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
# {'_id': ObjectId('5d6e9c24853a5739cc5db5bd'), 'item': 'canvas', 'qty': 100, 'tags': ['cotton'], 'size': {'h': 28, 'w': 35.5, 'uom': 'cm'}}


"""
Query Documents

To be continued
"""