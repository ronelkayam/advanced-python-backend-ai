"""
Title: MongoDB Audit Repository
Description: Handles all NoSQL persistence for audit and activity logs 
             using PyMongo, including connection verification and error handling.
"""

import logging
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import PyMongoError, ConnectionFailure

# Configure logging for clear tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class AuditMongoRepository:
    """
    Data Access Layer (Repository Pattern) for managing flexible 
    audit and activity logs in MongoDB (NoSQL Database).
    """

    def __init__(self, mongo_uri: str = "mongodb://localhost:27017/", db_name: str = "users_backend"):
        """Initializes the MongoDB client, verifies connection, and sets up the collection."""
        try:
            # Initialize client with a short timeout to prevent hanging if MongoDB is down
            self.client = MongoClient(mongo_uri, serverSelectionTimeoutMS=3000)
            self.client.admin.command('ping')  # Verify connection with a ping command

            self.db = self.client[db_name]
            self.collection = self.db['audit_logs']
            logging.info("[MongoDB] Connected successfully and audit collection is ready.")

        except (ConnectionFailure, PyMongoError) as e:
            logging.error(f"[MongoDB] Connection failed: {e}")
            self.client = None

    def log_event(self, user_id: int, username: str, action: str, metadata: dict = None) -> bool:
        """
        Inserts a flexible JSON/BSON audit log entry into MongoDB.
        Includes user ID, username, action type, timestamp, and optional metadata.
        """
        # Guard clause: Skip execution if the DB client failed to connect
        if self.client is None:
            logging.warning("[MongoDB] Skipping log entry; client is not connected!")
            return False

        try:
            log_entry = {
                "user_id": user_id,
                "username": username,
                "action": action,
                "timestamp": datetime.utcnow(),
                "metadata": metadata or {}  # Fallback to an empty dictionary if None
            }

            self.collection.insert_one(log_entry)
            logging.info(f"[MongoDB] Inserted log entry for user '{username}': {action}")
            return True

        except PyMongoError as e:
            logging.error(f"[MongoDB] Error inserting log entry: {e}")
            return False

    def get_user_logs(self, username: str) -> list:
        """
        Retrieves all audit logs associated with a specific username.
        Converts MongoDB's ObjectId to a string for clean serialization.
        """
        if self.client is None:
            logging.warning("[MongoDB] Cannot fetch logs; client is not connected.")
            return []

        try:
            # Query documents by username
            cursor = self.collection.find({"username": username})
            logs = list(cursor)

            # Convert ObjectId to string so it can be safely serialized (e.g. to JSON)
            for log in logs:
                log["_id"] = str(log["_id"])

            return logs

        except PyMongoError as e:
            logging.error(f"[MongoDB] Error fetching log entries for '{username}': {e}")
            return []