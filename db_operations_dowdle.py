# Project 5: Python and SQL
# This filentegrates Python and SQL, focusing on database interactions 
# using SQLite.

# import dependencies
import sqlite3
import pandas as pd
import pathlib
import logging

# Define the database file in the current root project directory
db_file = "C:\\Users\\Britt\\Documents\\44608\\datafun-05-sql\\project.db"

# Function to use pandas to read data from CSV files (in 'data' folder) and insert the records into 
#their respective tables.
def insert_data_from_csv():
    try:
        author_data_path = pathlib.Path("data", "authors.csv")
        book_data_path = pathlib.Path("data", "books.csv")
        authors_df = pd.read_csv(author_data_path)
        books_df = pd.read_csv(book_data_path)
        with sqlite3.connect(db_file) as conn:
            # Use the pandas DataFrame to_sql() method to insert data
            # Pass in the table name and the connection
            authors_df.to_sql("authors", conn, if_exists="replace", index=False)
            books_df.to_sql("books", conn, if_exists="replace", index=False)
            print("Data inserted successfully.")
    except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError) as e:
        print("Error inserting data from CSV:", e)

# Function to read and execute SQL statements to insert data
def insert_records():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = "C:\\Users\\Britt\\Documents\\44608\\datafun-05-sql\\sql\\insert_records.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Data inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting data from SQL:", e)

# Function to update one or more records in the authors table
def update_records():
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = "C:\\Users\\Britt\\Documents\\44608\\datafun-05-sql\\sql\\update_records.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records updated successfully.")
    except sqlite3.Error as e:
        print("Error updating records:", e)

# Function to delete records from a table
def delete_records():
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = "C:\\Users\\Britt\\Documents\\44608\\datafun-05-sql\\sql\\delete_records.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("Records deleted successfully.")
    except sqlite3.Error as e:
        print("Error deleting records:", e)

# Function to perform aggregation functions on the books table
def query_aggregation():
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = "C:\\Users\\Britt\\Documents\\44608\\datafun-05-sql\\sql\\query_aggregation.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            result = cursor.fetchone()
            print("Total Books:", result[0])
            print("Average Year Published:", round(result[1]))
            print("Oldest Book Published:", round(result[2]))
            print("Newest Book Published:", round(result[3]))
    except sqlite3.Error as e:
        print("Error querying aggregation for books:", e)

# Function to filter book data based on conditions
def query_filter():
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = "C:\\Users\\Britt\\Documents\\44608\\datafun-05-sql\\sql\\query_filter.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            books = cursor.fetchall()
            for book in books:
                print(book[1], book[2],)
    except sqlite3.Error as e:
        print("Error filtering book data:", e)        
        

#  Function to sort book data based on publication date
def query_sorting():
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = "C:\\Users\\Britt\\Documents\\44608\\datafun-05-sql\\sql\\query_sorting.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            books = cursor.fetchall()
            for book in books:
                print(book[0], book[1])
    except sqlite3.Error as e:
        print("Error sorting book data:", e)

# Function to execute SQL query with GROUP BY clause and display the count of each grouping
def query_group_by():
    try:
        db_file = pathlib.Path("project.db")
        with sqlite3.connect(db_file) as conn:
            sql_file = "C:\\Users\\Britt\\Documents\\44608\\datafun-05-sql\\sql\\query_group_by.sql"
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.cursor()
            cursor.execute(sql_script)
            results = cursor.fetchall()
            print("Length of Title Group:\tCount of Books:")
            for row in results:
                print(f"{row[0]}\t\t{row[1]}")
            print("Query executed successfully.")
    except sqlite3.Error as e:
        print("Error executing query:", e)

#  Function to read and execute SQL statements to perform INNER JOIN and display the results
def query_join():
    try:
        with sqlite3.connect(db_file) as conn:
            sql_file = pathlib.Path("query_join.sql")
            with open(sql_file, "r") as file:
                sql_script = file.read()
            cursor = conn.execute(sql_script)
            rows = cursor.fetchall()
            for row in rows:
                print(f"Author's First Name: {row[0]}, Title: {row[3]}")
            print("Query executed successfully.")
    except sqlite3.Error as e:
        print("Error executing query:", e)

# Python and SQL Integration
def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

# Define Main Function for SQL Operations Script
def main():
    insert_data_from_csv()
    insert_records()
    update_records()
    delete_records()
    query_aggregation()
    query_filter()
    query_sorting()
    query_group_by()
    query_join()

logging.info("All SQL operations completed successfully")

if __name__ == "__main__":
    logging.info("Program started") # add this at the beginning of the main method
    main()
    logging.info("Program ended")  # add this at the end of the main method