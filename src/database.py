import mysql.connector


# Global methods to push interact with the Database

# This method establishes the connection with the MySQL
def create_server_connection(host_name, user_name, user_password):
    # Implement the logic to create the server connection
    connection = None
    try:
        connection = mysql.connector.connect(user=user_name, password=user_password, host=host_name)
    except mysql.connector.Error as err:
        print(err)
    else:
        if connection.is_connected():
            print("Connected to Mysql")
    return connection


# This method will create the database and make it an active database
def create_and_switch_database(connection, db_name, switch_db):
    # For database creation use this method
    # If you have created your database using UI, no need to implement anything
    cursor = connection.cursor()
    try:
        drop_query = "DROP DATABASE IF EXISTS " + db_name
        db_query = "CREATE DATABASE " + db_name
        switch_query = "USE " + switch_db
        cursor.execute(drop_query)
        cursor.execute(db_query)
        cursor.execute(switch_query)
        print("Database created successfully")
    except mysql.connector.Error as err:
        print(f"Error in creating database: '{err}'")


# This method will establish the connection with the newly created DB
def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(user=user_name, password=user_password, host=host_name, database=db_name)
    except mysql.connector.Error as err:
        print(err)
    return connection


# Use this function to create the tables in a database
def create_table(connection, table_creation_statement):
    cursor = connection.cursor()
    try:
        cursor.execute(table_creation_statement)
        connection.commit()
        print("Table creation successful")
    except Exception as err:
        print(f"Error in table_creation: '{err}'")


# Perform all single insert statements in the specific table through a single function call
def create_insert_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Insert operation successful")
    except Exception as err:
        print(f"Error in insert query: '{err}'")


# retrieving the data from the table based on the given query
def select_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print(f"Error in select query: '{err}'")


# Execute multiple insert statements in a table
def insert_many_records(connection, sql, val):
    cursor = connection.cursor()
    try:
        cursor.executemany(sql, val)
        connection.commit()
        print("Many Insert operations are successful")
    except Exception as err:
        print(f"Error in many insert query: '{err}'")
