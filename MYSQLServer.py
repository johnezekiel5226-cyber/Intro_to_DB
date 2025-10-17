# MySQLServer.py

import mysql.connector
from mysql.connector import errorcode

# Configuration for database connection
config = {
    'user': 'root',  # <--- REPLACE THIS
    'password': 'Naijaloaded123@', # <--- REPLACE THIS
    'host': '127.0.0.1'
}

DATABASE_NAME = 'alx_book_store'

cnx = None
cursor = None

try:
    # 1. Connect to MySQL server
    print(f"Attempting to connect to MySQL server at {config['host']}...")
    cnx = mysql.connector.connect(**config)
    print("Connection established successfully.")

    # 2. Create a cursor object
    cursor = cnx.cursor()

    # 3. Execute the SQL command
    # CREATE DATABASE IF NOT EXISTS prevents failure if the DB already exists
    sql_command = f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"
    cursor.execute(sql_command)

    # Print the success message as required
    print(f"Database '{DATABASE_NAME}' created successfully!")
    
except mysql.connector.Error as err:
    # Handle connection/server errors
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Error: Access denied. Check your username and password.")
    else:
        print(f"Error connecting to the database: {err}")
    
finally:
    # 4. Handle open and close of the DB connection
    # Close the cursor and connection if they were opened
    if cursor:
        cursor.close()
    if cnx and cnx.is_connected():
        cnx.close()
    print("Database operation complete.")
