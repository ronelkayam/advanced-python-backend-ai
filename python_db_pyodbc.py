"""
===================================================================
 Topic: Python Database Connectivity with pyodbc & SQL Server
===================================================================

Description:
This file demonstrates how to connect directly to a Microsoft SQL Server database
using the `pyodbc` library, execute a SQL query, and process the results:
1. Connection String: Configuration for connecting to a local SQL Server
   instance (Northwind database) using Windows Authentication via ODBC Driver 17.
2. Cursors: Utilizing a database cursor (`conn.cursor()`) to execute SQL statements
   and iterate over the retrieved result sets.
3. Resource Management: Explicitly managing connection lifecycles using `try-except-finally`
   blocks to ensure cursors and connections are properly closed.
4. Result Processing: Fetching all rows (`cursor.fetchall()`) and parsing them dynamically.

Key Takeaways:
- Direct use of `pyodbc` provides low-level control over ODBC connections.
- Always ensure database connections and cursors are closed (via `try...finally`)
  to avoid connection leaks and unreleased server resources.
"""

import pyodbc

# Connection string to local server - Windows Authentication
connection_string = (
    'Driver={ODBC Driver 17 for SQL Server};'
    'Server=localhost;'
    'Database=Northwind;'
    'Trusted_Connection=yes;'
)

try:
    # Open connection and create a cursor
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    # Define the SQL query to filter products by price range
    query = """
        select ProductName, UnitPrice, UnitsInStock
        from Products
        where UnitPrice > 20 and UnitPrice < 50
    """

    # Execute the query
    cursor.execute(query)

    # Print all rows retrieved from the database
    print("---- כל המוצרים שעונים על התנאי של השאילתא -----")
    for row in cursor.fetchall():
        print(f"product name: {row.ProductName}| price: {row.UnitPrice}| stock: {row.UnitsInStock}")

except Exception as e:
    # Catch and display any connection or execution errors
    print(f"Failed vs DB: {e}")

finally:
    # Ensure resources are cleanly released regardless of success or failure
    cursor.close()
    conn.close()