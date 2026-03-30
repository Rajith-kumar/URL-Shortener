import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Rajith@123",
        database="url_shortener"
    )