from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

LOGIN = "megaz0rd"
HOST = "localhost"
PASSWORD = "coderslab"
DATABASE = "postgres"

CREATE_DB = "CREATE DATABASE members;"

CREATE_TABLE_USERS = """
    CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    hashed_password varchar(80)
);
"""

CREATE_TABLE_MESSAGES = """
    CREATE TABLE messages(
    id SERIAL PRIMARY KEY,
    from_id INT REFERENCES users(id) ON DELETE CASCADE,
    to_id INT REFERENCES users(id) ON DELETE CASCADE,
    text VARCHAR(255),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
"""

try:
    with connect(user=LOGIN, password=PASSWORD, host=HOST, database=DATABASE) \
            as connection:
        connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(CREATE_DB)
            print("Database created")
        except DuplicateDatabase as e:
            print("Sorry,", e)
except OperationalError as ex:
    print("Connection Error", ex)

try:
    with connect(user=LOGIN, password=PASSWORD, host=HOST,
                 database="members") as connection:
        connection.autocommit = True
        cursor = connection.cursor()
        try:
            cursor.execute(CREATE_TABLE_USERS)
            print("Table created")
        except DuplicateTable as e:
            print("Table and", e)

        try:
            cursor.execute(CREATE_TABLE_MESSAGES)
            print("Table created")
        except DuplicateTable as e:
            print("Table and", e)
except OperationalError as e:
    print("Connection Error:", e)
