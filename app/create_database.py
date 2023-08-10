import os

from dotenv import load_dotenv
from mysql import connector

env_file_path = '../.env'

load_dotenv()
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("SERVER")
USERNAME = 'root'
DATABASE_NAME = "USERS"


try:
    with connector.connect(
        host = HOST,
        user = USERNAME,
        password = PASSWORD
    ) as database: 
        print(f"Database object: {database}")
        create_database_query = f"CREATE DATABASE {DATABASE_NAME};"
        with database.cursor() as cursor:
            cursor.execute(create_database_query)

        print(f'database {DATABASE_NAME} complate!')

except connector.Error as e: 
    print(e)

