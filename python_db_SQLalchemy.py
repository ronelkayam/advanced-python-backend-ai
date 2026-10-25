"""
===================================================================
 Topic: Python Database Connectivity with SQLAlchemy & SQL Server
===================================================================

Description:
This file demonstrates how to connect to a Microsoft SQL Server database
using SQLAlchemy and pyodbc, execute a secure parameterized query, and
process the results:
1. Connection String: Configuration for connecting to a local SQL Server 
   instance (Northwind database) using Windows Authentication.
2. Connection Management: Using a context manager (`with` statement) to 
   ensure connections are properly opened and closed automatically.
3. Parameterized Queries: Using SQLAlchemy's `text()` construct along with 
   named parameters (`:max_price`) to prevent SQL Injection.
4. Error Handling: Catching connection and execution exceptions gracefully.

Key Takeaways:
- Never use string concatenation/formatting for SQL queries with user inputs; 
  always use parameterized queries to protect against SQL Injection.
- Context managers guarantee resource cleanup, preventing database connection leaks.
"""

from sqlalchemy import create_engine, text

# Define the database connection engine using SQLAlchemy and pyodbc driver
engine = create_engine(
    "mssql+pyodbc:///?odbc_connect="
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=Northwind;"
    "Trusted_Connection=yes;"
)

try:
    # Establish a secure connection using a context manager
    with engine.connect() as connection:

        # Define a parameterized SQL query
        query = text("""
            SELECT ProductName, UnitPrice
            FROM Products 
            WHERE UnitPrice > :max_price
        """)

        # Execute the query, passing parameters safely as a dictionary
        result = connection.execute(query, {"max_price": 30})

        print("------ Prices of products more expensive than 30 ------")

        # Iterate through the result rows and display data dynamically
        for row in result:
            print(f"{row.ProductName}: ${row.UnitPrice}")

except Exception as e:
    # Catch and report any connection or execution errors
    print(f"Failed to connect to DB: {e}")