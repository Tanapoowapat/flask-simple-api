from mysql import connector
from dotenv import load_dotenv
import os

env_path = "../.env"

load_dotenv()
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("SERVER")
USERNAME = 'root'
DATABASE_NAME = "USERS"

class Database:
    def __init__(self):
        self.conn = connector.connect(
            host =HOST,
            username = USERNAME,
            password = PASSWORD,
            database = DATABASE_NAME
        )
        self.cursor = self.conn.cursor()
 
    def create_user(self, uid, name, age):
        query = "INSERT INTO USER (uid, name, age) VALUES (%s, %s, %s);"
        value = (uid, name, age)
        self.cursor.execute(query, value)
        self.conn.commit()

    def get_users(self):
        query = "SELECT * FROM USER;"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_user(self, uid):
        qurey = "SELECT * FROM USER WHERE uid =%s;"
        self.cursor.execute(qurey, (uid,))
        return self.cursor.fetchone()
    
    def delete_user(self, uid):
        qurey = "DELETE FROM USER WHERE uid = %s;"
        self.cursor.execute(qurey, (uid,))
        self.conn.commit()

    def update(self, uid, name, age):
        qurey = "UPDATE USER SET name = %s, age = %s WHERE uid = %s;"
        val = (name, age, uid)
        self.cursor.execute(qurey, (val))
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()