import psycopg2
import json
from loguru import logger

DATABASE_CONFIG = {
    'dbname': 'db',
    'user': 'admin',
    'password': 'root',
    'host': 'localhost'
}

SCHEMA_NAME = 'data'
TABLE_NAME = f"{SCHEMA_NAME}.temp_data"

def store_in_postgres(data):
    connection = psycopg2.connect(**DATABASE_CONFIG)
    cursor = connection.cursor()

    # Assuming you've created a table called 'temp_data' with columns 'data' and 'id'
    insert_query = f"""INSERT INTO {TABLE_NAME} (data) VALUES (%s);"""
    cursor.execute(insert_query, (data,))

    connection.commit()
    cursor.close()
    connection.close()
