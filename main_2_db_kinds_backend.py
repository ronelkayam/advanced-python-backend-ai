"""
Title: Hybrid User Facade & Execution Script
Description: Coordinates the business logic between the Relational database 
             (SQL Server) and the NoSQL database (MongoDB). Includes a 
             demonstration execution block for testing the complete workflow.
"""

import logging
import pprint

# Configure global logging format for clear tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Import custom repository layers
from sqlserver_repository import sqlServerUserRepository
from mongodb_repository import AuditMongoRepository


class HybridUserFacade:
    """
    Service layer (Facade Pattern) responsible for orchestrating 
    operations across multiple disparate databases (SQL Server + MongoDB).
    """

    def __init__(self, user_repo: sqlServerUserRepository, audit_repo: AuditMongoRepository):
        """Initializes the facade with injected database repository instances."""
        self.user_repo = user_repo
        self.audit_repo = audit_repo

    def register_new_user(self, username: str, email: str, metadata: dict = None) -> bool:
        """
        Orchestrates the hybrid user registration process:
        1. Inserts core user entity into SQL Server.
        2. If successful, records a dynamic activity/audit log in MongoDB.
        """
        # Step 1: Save core transactional data in SQL Server
        user_id = self.user_repo.create_user(username, email)
        if not user_id:
            logging.warning(f"Registration failed for user '{username}': User already exists or DB error.")
            return False  # Registration Failed!

        # Step 2: Save flexible audit trail in MongoDB
        self.audit_repo.log_event(
            user_id=user_id,
            username=username,
            action="Registered",
            metadata=metadata or {}
        )

        logging.info(f"User '{username}' successfully registered across both databases.")
        return True

    def get_complete_profile(self, username: str) -> dict:
        """
        Aggregates data from both databases:
        - Core profile information from SQL Server.
        - Activity and audit history logs from MongoDB.
        """
        # Fetch core structured data from Relational DB
        user_profile = self.user_repo.get_by_username(username)
        if not user_profile:
            logging.warning(f"Profile aggregation failed: User '{username}' not found.")
            return None

        # Fetch flexible unstructured logs from NoSQL DB
        activity_logs = self.audit_repo.get_user_logs(username)

        # Return combined aggregated view
        return {
            "profile": user_profile,
            "activity_logs": activity_logs
        }


# --- Demonstration Execution Block ---
if __name__ == '__main__':
    print("=== Starting Hybrid User Facade Demo ===\n")

    # 1. Initialize individual database repositories
    sql_server_repo = sqlServerUserRepository()
    mongo_repo = AuditMongoRepository(mongo_uri="mongodb://localhost:27017/users_backend")

    # 2. Inject repositories into the Facade service
    backend_service = HybridUserFacade(sql_server_repo, mongo_repo)

    # 3. Simulate registering a new user with dynamic metadata
    success = backend_service.register_new_user(
        username="Nitzan_dev",
        email="nitzan@gmail.com",
        metadata={
            "ip": "172.16.31.10",
            "os": "Ubuntu 22.04",
            "course": "Backend Engineering"
        }
    )

    # 4. If registration succeeded, fetch and print the combined profile view
    if success:
        complete_view = backend_service.get_complete_profile(username="Nitzan_dev")
        print("\n---- Aggregated Profile Result ----")
        pprint.pprint(complete_view)