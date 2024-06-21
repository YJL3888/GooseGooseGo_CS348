import mysql.connector
import os
import bcrypt


def create_connection():
    """Create a database connection to the database"""
    return mysql.connector.connect(
        host='goosegoosego.clegmk4ois3q.us-east-1.rds.amazonaws.com',
        user='admin',
        password=os.getenv('DB_PASSWORD'),
        database='sample_data'
    )

def hash_password(password):
    """Hash a password for storing."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def select_food_items(conn):
    """Query the database and print the results."""
    with conn.cursor() as cursor:
        query = "SELECT * FROM food_items"
        cursor.execute(query)
        rows = cursor.fetchall()

        print('Printing food items')
        for row in rows:
            print(row)


if __name__ == '__main__':
    with create_connection() as connection:
        select_food_items(connection)
