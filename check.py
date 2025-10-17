import mysql.connector

# --- Configuration (replace credentials) ---
config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': '127.0.0.1'
}

cnx = None

try:
    # 1. Attempt connection
    cnx = mysql.connector.connect(**config)
    
    # 2. Explicitly check and print success message
    if cnx.is_connected():
        print("Connection **Successful!** Database server is reachable.")
        # Proceed with database creation (cursor = cnx.cursor(), etc.)
    else:
        # Fallback if connect() didn't raise an error but connection state is bad
        print("Connection **Failed** after initial attempt.")

except mysql.connector.Error as err:
    # Handle all connection failures
    print(f"Connection **Failed** with Error: {err}")
    
finally:
    # 3. Always close the connection if it was opened
    if cnx and cnx.is_connected():
        cnx.close()