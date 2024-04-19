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
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


connection_one = create_connection("localhost", 3306, "root", "root", "user")
connection_two = create_connection("localhost", 3307, "root", "root", "user")

# SQL Insert query

i = 0
while i < 10:
    value = "perul-" + str(i)
    print(value)
    i = i + 1
    insert_query = """
        INSERT INTO user (name)
        VALUES (%s)
        """
    if i%2==0:
        # Execute the query
        execute_query(connection_one, insert_query, (value,))
    else:
        execute_query(connection_two, insert_query, (value,))

    
    



