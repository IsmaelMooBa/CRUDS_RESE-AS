import mysql.connector

database =  mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='crud_products_py',
)

if database.is_connected():
    print("Conexión exitosa")
    