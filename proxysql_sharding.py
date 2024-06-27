import mysql.connector
from mysql.connector import Error

def create_connection(host_name, port, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            port = port,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def execute_query(connection, query, value):
    cursor = connection.cursor()
    try:
        cursor.execute(query, value)
        connection.commit()
        print("Query executed successfully " + query)
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection("localhost", 6033, "root", "root", "user")


i = 1
while i <= 20:
    value = "perul-" + str(i)
    print(value)
    insert_query = """INSERT INTO user (id, name) VALUES (%s, %s)"""
    execute_query(connection, insert_query, (i,value,))
    i = i + 1