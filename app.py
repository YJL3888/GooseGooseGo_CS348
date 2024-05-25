import mysql.connector
from mysql.connector import Error
# pip install mysql-connector-python

import os

def create_connection():
    """Create a database connection to the database"""
    connection = None
    try:
        connection = mysql.connector.connect(
            host='goosegoosego.clegmk4ois3q.us-east-1.rds.amazonaws.com',
            user='admin',
            password=os.getenv('DB_PASSWORD'),
            database='sample_db'
        )
        print('Connection to MySQL DB successful')
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def select_food_items(connection):
    """Query the database and print the results."""
    cursor = connection.cursor()
    query = "SELECT * FROM food_items"
    cursor.execute(query)
    rows = cursor.fetchall()

    print('Printing food items')
    for row in rows:
        print(row)
    cursor.close()

def main():
    connection = create_connection()
    if connection is not None:
        select_food_items(connection)
        connection.close()

if __name__ == '__main__':
    main()
