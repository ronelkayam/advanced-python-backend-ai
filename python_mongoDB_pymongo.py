"""
Introduction to MongoDB with Python (PyMongo) from scratch

Description:
This file demonstrates the foundational steps of interacting with a
NoSQL DB using python and PyMongo:
1. Client connection: Establish a connection to the local MongoDB server
2. DB & Collection Access: Navigating to the 'DB_name' db
   and the 'Collection_name' collection
3. Querying Data: Using filter operation (for example $gt for greater than)
to retrieve specific documents
4. Data Parsing: Extracting field dynamically from JSON documents
   (which map directly to python dictionaries).

Key Takeaways:
- NoSQL db don't require a fixed table schema, documents are sorted
  as flexible JSON structures
- PyMongo query dictionaries directly into MongoDB DB queries
"""

from pymongo import MongoClient

# 1. Establish connection to the local MongoDB instance
# Default port from MongoDB is 27017
client = MongoClient("mongodb://localhost:27017/")

try:
    # 2. Access the db and collection(created in compass)
    db = client["Northwind"]
    products_collection = db["Products"]

    # 3. Define a query filter (equivalent to WHERE UnitPrice>30 in SQL)
    # Here we look for documents where UnitPrice is greater then 30
    query_filter = {"UnitPrice": {"$gt": 30}}

    # 4. Execute the query and resulting documents and display their data
    cursor = products_collection.find(query_filter)

    print("************ MongoDB products more expensive then 30 ********")
    # Iterate through the resulting documents and display their data
    found_any = False
    for document in cursor:
        found_any = True
        product_name = document.get("ProductName")
        unit_price = document.get("UnitPrice")
        units_in_stock = document.get("UnitInStock")

        print(f"Product: {product_name} | UnitPrice: {unit_price} | UnitInStock: {units_in_stock}")

        if not found_any:
            print("No product found!!")


except Exception as e:
    # 5. Handle connection or query errors gracefully
    print(f"Failed to interact with MongoDB : {e}")

finally:
    # 6. Always close the client connection when done
    client.close()
