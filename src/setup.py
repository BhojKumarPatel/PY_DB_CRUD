import csv
import database as db

PW = "Password"  # IMPORTANT! Put your MySQL Terminal password here.
ROOT = "root"
DB = "ecommerce_record"  # This is the name of the database we will create in the next step - call it whatever you like.
LOCALHOST = "localhost"  # considering you have installed MySQL server on your computer

RELATIVE_CONFIG_PATH = '../config/'

USER = 'users'
PRODUCTS = 'products'
ORDER = 'orders'

# Create the tables through python code here
# if you have created the table in UI, then no need to define the table structure
# If you are using python to create the tables, call the relevant query to complete the creation
# Create User Table
create_user_table_if_not_exist = """CREATE TABLE IF NOT EXISTS users (
    user_id VARCHAR(10) NOT NULL PRIMARY KEY,
    user_name VARCHAR(45) NOT NULL,
    user_email VARCHAR(45) NOT NULL,
    user_password VARCHAR(45) NOT NULL,
    user_address VARCHAR(45) NOT NULL,
    is_vendor TINYINT(1) DEFAULT 0
)
"""

# Products Table creation
create_product_table_if_not_exist = """CREATE TABLE IF NOT EXISTS products (
    product_id VARCHAR(45) NOT NULL PRIMARY KEY,
    product_name VARCHAR(45) NOT NULL,
    product_price FLOAT NOT NULL,
    product_description VARCHAR(100) NOT NULL,
    vendor_id VARCHAR(10) NOT NULL,
    emi_available VARCHAR(10) NOT NULL,
    CONSTRAINT fk_vendor_id FOREIGN KEY (vendor_id) REFERENCES users (user_id)
)
"""

# Create Order Table
create_orders_table_if_not_exist = """CREATE TABLE IF NOT EXISTS orders (
    order_id INT NOT NULL PRIMARY KEY,
    customer_id VARCHAR(10),
    vendor_id VARCHAR(10) NOT NULL,
    total_value FLOAT NOT NULL,
    order_quantity INT NOT NULL,
    reward_point INT NOT NULL,
    CONSTRAINT fk_customer_id FOREIGN KEY (customer_id) REFERENCES users (user_id)
    )
"""

# Create Customer Leaderboard Table
create_customer_leaderboard_table_if_not_exist = """CREATE TABLE IF NOT EXISTS customer_leaderboard (
    customer_id VARCHAR(10) NOT NULL PRIMARY KEY,
    total_value FLOAT NOT NULL,
    customer_name VARCHAR(45) NOT NULL,
    customer_email VARCHAR(50) NOT NULL
)
"""
print("\n-------------E-Commerce Solution----------- \n")
print("\n----Solution Problem 1.a-----")
connection = db.create_server_connection(LOCALHOST, ROOT, PW)

# creating the schema in the DB
db.create_and_switch_database(connection, DB, DB)
print("-------Solution 1.a Completed------\n")

print("\n----Solution Problem 1.b-----\n Table creation initiated:\n")
db.create_table(connection, create_user_table_if_not_exist)
print("****User Table Created****\n")
db.create_table(connection, create_product_table_if_not_exist)
print("****Product Table Created****\n")
db.create_table(connection, create_orders_table_if_not_exist)
print("****Orders Table Created****\n")
db.create_table(connection, create_customer_leaderboard_table_if_not_exist)
print("****Customer Leader Board Table Created****\n")
print("-------Solution 1.b Completed------\n")

print("\n----Solution Problem 2.a-----")
print("\nInitiating data entry for users table\n")
with open(RELATIVE_CONFIG_PATH + USER + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))

    sql = """INSERT INTO users (user_id, user_name, user_email, user_password, user_address, is_vendor)
    VALUES(%s, %s, %s, %s, %s, %s)
    """
    val.pop(0)
    db.insert_many_records(connection, sql, val)
print("\n----- Data insertion to Users completed -------- \n")

"""
    Here we have accessed the file data and saved into the val data structure, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """
print("\nInitiating data entry for products table\n")
with open(RELATIVE_CONFIG_PATH + PRODUCTS + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))
    sql = """INSERT INTO products (product_id, product_name, product_price, product_description, vendor_id, emi_available)
        VALUES(%s, %s, %s, %s, %s, %s)
        """
    val.pop(0)
    db.insert_many_records(connection, sql, val)
print("\n----- Data insertion to Products completed -------- \n")
"""
    Here we have accessed the file data and saved into the val data structure, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """

print("\nInitiating data entry for orders table\n")
with open(RELATIVE_CONFIG_PATH + ORDER + '.csv', 'r') as f:
    val = []
    data = csv.reader(f)
    for row in data:
        val.append(tuple(row))

    sql = """INSERT INTO orders (order_id, customer_id, vendor_id, total_value, order_quantity, reward_point)
        VALUES(%s, %s, %s, %s, %s, %s)
        """
    val.pop(0)
    db.insert_many_records(connection, sql, val)
print("\n----- Data insertion to Orders completed -------- \n")

print("----- Problem 2.a Completed -------- \n")

"""
    Here we have accessed the file data and saved into the val data structure, which list of tuples. 
    Now you should call appropriate method to perform the insert operation in the database. 
    """