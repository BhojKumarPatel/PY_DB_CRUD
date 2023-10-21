import database as db
import setup as set

# Driver code
if __name__ == "__main__":
    """
    Please enter the necessary information related to the DB at this place. 
    Please change PW and ROOT based on the configuration of your own system. 
    """
    PW = "Password"  # IMPORTANT! Put your MySQL Terminal password here.
    ROOT = "root"
    DB = "ecommerce_record"  # This is the name of the database we will create in the next step - call it whatever
    # you like.
    LOCALHOST = "localhost"
    connection = db.create_db_connection(LOCALHOST, ROOT, PW, DB)

    # creating the schema in the DB 
    #db.create_and_switch_database(connection, DB, DB)




    # Start implementing your task as mentioned in the problem statement 
    # Implement all the test cases and test them by running this file
    print("\n--------Problem 2.b solution -------")
    print("\nInserting additional 5 orders in Orders Table")
    new_orders = """INSERT INTO orders (order_id, customer_id, vendor_id, total_value, order_quantity, reward_point)
        VALUES (1001, 14, 4, 12456, 2, 100),
        (1002, 1, 5, 2356, 3, 200),
        (1003, 10, 6, 4578, 5, 300),
        (1004, 9, 7, 5689, 6, 300),
        (1005, 7, 9, 6790, 7, 300);
    """

    db.create_insert_query(connection, new_orders)
    print("--------Problem 2.b complete -------\n")

    print("\n--------Problem 2.c solution -------")
    orders_query = "Select * from orders;"
    orders = db.select_query(connection, orders_query)
    for order in orders:
        print(order)

    print("--------Problem 2.c complete -------\n")

    print("\n--------Problem 3.a solution -------")
    min_orders_query = """SELECT * FROM orders
    WHERE total_value = (SELECT MIN(total_value) FROM orders);"""

    min_order = db.select_query(connection, min_orders_query)
    print("Order With Minimum Value Details:")
    print(min_order)

    max_orders_query = """SELECT * FROM orders
        WHERE total_value = (SELECT MAX(total_value) FROM orders);"""

    max_order = db.select_query(connection, max_orders_query)
    print("Order With Max Value Details:")
    print(max_order)

    print("--------Problem 3.a complete -------\n")

    print("\n--------Problem 3.b solution -------")
    print("List of orders value greater than average value")
    orders_greater_avg_val = """ SELECT * FROM orders 
    WHERE total_value > (SELECT AVG(total_value) FROM orders);
    """
    val = db.select_query(connection, orders_greater_avg_val)
    for order in val:
        print(order)

    print("--------Problem 3.b complete -------\n")

    print("\n--------Problem 3.c solution -------")

    print("\n Fetching Customer Details with max value order")
    query = """SELECT o.customer_id, MAX(o.total_value) as Max_value, u.user_name, u.user_email
    from ecommerce_record.orders o
    LEFT JOIN ecommerce_record.users u ON o.customer_id = u.user_id
    GROUP BY o.customer_id
    """

    highest_purchase_per_customer = db.select_query(connection, query)

    insert_query = """INSERT INTO customer_leaderboard (customer_id, total_value, customer_name, customer_email)
    VALUES(%s, %s, %s, %s)"""

    print("\n Initialising data insertion to customer_leaderboard table \n")

    db.insert_many_records(connection, insert_query, highest_purchase_per_customer)
    print("\n Data insertion to customer_leaderboard table Completed \n")
    print("--------Problem 3.c complete -------\n")

    print("******* Printing Leader Board Details")
    leaderboard_query = "Select * from customer_leaderboard ORDER BY total_value desc;"
    leaders = db.select_query(connection, leaderboard_query)
    for lead in leaders:
        print(lead)
