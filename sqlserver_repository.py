"""
Title: SQL Server User Repository
Description: Handles all Relational database persistence and queries for users 
             using pyodbc, with OUTPUT INSERTED.id for clean ID retrieval.
"""

import logging
from datetime import datetime
import pyodbc

# Configure logging for clear tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class sqlServerUserRepository:
    """
    Data Access Layer (Repository Pattern) for managing user records 
    in SQL Server (Relational Database) using pyodbc.
    """

    def __init__(self, connection_string: str = "DRIVER={ODBC Driver 17 for SQL Server};"
                                                "SERVER=localhost;"
                                                "DATABASE=users_backend_hacker_u;"
                                                "Trusted_connection=yes;") -> None:
        """Initializes the repository with a connection string and ensures the users table exists."""
        self.conn_str = connection_string
        self._init_table()

    def _init_table(self):
        """Checks if the 'users' table exists in SQL Server, and creates it if it doesn't."""
        try:
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='users' AND xtype='U')
                    CREATE TABLE users(
                        id INT IDENTITY(1,1) PRIMARY KEY,
                        username NVARCHAR(100) UNIQUE NOT NULL,
                        email NVARCHAR(255) NOT NULL,
                        created_at DATETIME NOT NULL
                    )
                ''')
                conn.commit()
                logging.info("[SQL SERVER] Users table checked/created successfully.")

        except pyodbc.Error as e:
            logging.error(f"[SQL SERVER] Initialization error: {e}")
            raise

    def create_user(self, username: str, email: str) -> int:
        """
        Inserts a new user into SQL Server and retrieves the newly generated ID 
        instantly using the OUTPUT INSERTED.id clause.
        """
        try:
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()
                created_at = datetime.utcnow()

                # Use OUTPUT INSERTED.id to return the new ID directly from the insert statement
                cursor.execute(
                    "INSERT INTO users (username, email, created_at) "
                    "OUTPUT INSERTED.id "
                    "VALUES (?, ?, ?);",
                    (username, email, created_at)
                )

                row = cursor.fetchone()
                user_id = int(row[0]) if row and row[0] is not None else None

                conn.commit()
                logging.info(f"[SQL SERVER] User '{username}' inserted with ID {user_id}.")
                return user_id

        except pyodbc.IntegrityError:
            logging.warning(f"[SQL SERVER] User '{username}' already exists (Constraint violation).")
            return None
        except pyodbc.Error as e:
            logging.error(f"[SQL SERVER] Error while inserting user: {e}")
            raise

    def get_by_username(self, username: str) -> dict:
        """
        Retrieves a single user record by username and maps it to a dictionary.
        """
        try:
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()

                cursor.execute(
                    "SELECT id, username, email, created_at FROM users WHERE username = ?;",
                    (username,)
                )
                row = cursor.fetchone()

                if not row:
                    return None

                columns = [column[0] for column in cursor.description]
                return dict(zip(columns, row))

        except pyodbc.Error as e:
            logging.error(f"[SQL SERVER] Error while getting user '{username}': {e}")
            return None