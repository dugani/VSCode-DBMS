import mysql.connector
from mysql.connector import Error
import random
import time
import datetime
import csv



# Global methods to push interact with the Database

# This method establishes the connection with the MySQL
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_server_connection("localhost", "root", "ILikeIreland_1")

# This method will create the database and make it an active database
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err}'")

create_database_query = "CREATE DATABASE ecommerce"
create_database(connection, create_database_query)



# This method will establish the connection with the newly created DB
def create_db_connection(host_name, user_name, user_password,db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
            )
        print(" Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

connection = create_db_connection("localhost", "root", "ILikeIreland_1","ecommerce_record")



# Use this function to create the tables in a database

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

create_Zord_table = """
CREATE TABLE Zord (
  order_id INT primary key,
  customer_id INT,
  vendor_id INT,
  total_value INT,
  order_quantity INT,
  reward_points INT
  );
 """

create_Zprod_table = """
CREATE TABLE Zprod (
  product_id varchar(45) primary key,
  product_name varchar(30),
  product_price INT,
  product_description varchar(30),
  vendor_id INT,
  emi_avalaible varchar(20)
  );
 """

create_Zusers_table = """
CREATE TABLE Zusers (
  user_id varchar(10) primary key,
  user_name varchar(30),
  user_email varchar(30),
  user_password varchar(30),
  user_address varchar(30),
  is_vendor INT
  );
 """

alter_Zord = """
ALTER TABLE Zord
customer_id varchar(10),
vendor_id varchar(10),
ADD FOREIGN KEY(vendor_id)
REFERENCES Zord(vendor_id)
ADD FOREIGN KEY(customer_id)
REFERENCES Zord(customer_id)
ON DELETE SET NULL;
"""

alter_Zprod = """
ALTER TABLE Zprod
product_name varchar(45),
product_price DOUBLE,
product_description varchar(100),
emi_avalaible varchar(20)
vendor_id varchar(10),
ADD FOREIGN KEY(vendor_id)
REFERENCES Zprod(vendor_id)
ON DELETE SET NULL;
"""
alter_Zusers = """
ALTER TABLE Zusers
user_name varchar(45),
user_email varchar(45),
user_password varchar(45),
user_address varchar(45),
is_vendor TINYINT(1),
ADD FOREIGN KEY(vendor_id)
REFERENCES Zprod(vendor_id)
ON DELETE SET NULL;
"""

# connection = create_db_connection("localhost", "root", "ILikeIreland", "ecommerce")
execute_query(connection, create_Zord_table) # Execute our defined query
execute_query(connection, create_Zprod_table)
execute_query(connection, create_Zusers_table)
execute_query(connection, alter_Zord)
execute_query(connection, alter_Zprod)
execute_query(connection, alter_Zusers)

# Perform all single insert statments in the specific table through a single function call
def create_insert_query(connection, query):
    # This method will perform creation of the table
    # this can also be used to perform single data point insertion in the desired table
    pass


# retrieving the data from the table based on the given query
def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")
q1 = """
SELECT *
FROM orders;
"""
connection = create_db_connection("localhost", "root", "ILikeIreland_1", "ecommerce_record")
results = read_query(connection, q1)

for result in results:
  print(result)


def select_query(connection, query):
    # fetching the data points from the table 
    pass


# Execute multiple insert statements in a table
def insert_many_records(connection, sql, val):
    pass
