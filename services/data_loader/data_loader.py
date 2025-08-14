import mysql.connector
import os
from mysql.connector import Error

class DataLoader:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv("MYSQL_HOST"),
                user=os.getenv("MYSQL_USER"),
                password=os.getenv("MYSQL_PASSWORD"),
                database=os.getenv("MYSQL_DATABASE")
            )
            if not self.conn.is_connected():
                raise Error("Failed to connect to MySQL")
        except Error as e:
            raise RuntimeError(f"MySQL connection error: {e}")

    def get_data(self):
        try:
            with self.conn.cursor(dictionary=True) as cursor:
                cursor.execute("SELECT * FROM data")
                return cursor.fetchall()
        except Error as e:
            print(f"Error reading data: {e}")
            return []
        finally:
            if self.conn.is_connected():
                self.conn.close()
