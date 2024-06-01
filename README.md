# datafun-05-sql

## Overview
Project 5 integrates Python and SQL, focusing on database interactions using SQLite. This project introduces logging, a useful tool for debugging and monitoring projects, and involves creating and managing a database, building a schema, and performing various SQL operations, including queries with joins, filters, and aggregations.

CC5.1: Start a new Project

+ Create a GitHub project repository with a default README.md.
+ Clone your repo down to your machine. 
+ Open your project folder in VS Code (if you haven't already).
+ Add a useful .gitignore with a line for .vsode/ and .venv/ and whatever else doesn't need to go in the repo. 

## How to Install and Run the Project

### Clone Your Repo

```shell
git clone "paste_your_repo_URL_here"
```

### Create Project Virtual Environment

On Windows, create a project virtual environment in the .venv folder. 

```shell
py -m venv .venv
.venv\Scripts\Activate
pip list
py -m pip install --upgrade pip
deactivate
```

### Create files in root folder

```shell
# Example for managing project requirements
code .
ni "requirements.txt"
```

### Add all dependencies by installing packages seperately
```shell
#Example If you have a requirements.txt list each package in this file
py -m pip install -r requirements.txt
#Example If you don't
py -m pip install jupyterlab numpy pandas matplotlib seaborn scipy
```

### Freeze Your Dependencies
This will keep the package at the version it was installed as
```shell
py -m pip freeze > requirements.txt
```

### Git add and commit 

```shell
git add .
git commit -m "initial commit"
git push origin main
```

CC5.3 Plan the Project / Gather Data

+ Create subfolder for SQL statements
+ Create subfolder for data files
+ Create 2 .csv files in data folder

>![Screenshot of VS Code root folder options to create subfolders](https://github.com/Bdowdle4/datafun-05-sql/blob/main/Screenshots/Screenshot%202024-05-31%20184726.png)
>
> To create the subfolders sql and data, click on the second icon from the left with the + sign.
>
>![Screenshot of VS Code subfolder options to create files](https://github.com/Bdowdle4/datafun-05-sql/blob/main/Screenshots/Screenshot%202024-05-31%20185302.png)
>
> To create the files in the data folder, click onto the folder, then click on the first icon from the left with the + sign.

CC5.4 Initialize the Database

+ Create 2 .sql statements in the subfolder sql
+ Create a .py file to store your script
+ Create a .db file to define your database

>![Screenshot of VS Code root folder containing new files created following the steps in previous CC5.3 Notice how each type of file receives its own icon. This visual reference helps to access files quickly](https://github.com/Bdowdle4/datafun-05-sql/blob/main/Screenshots/Screenshot%202024-05-31%20190241.png)
>
> You will need to use an extension or search the web for a SQL viewer to see the output of the .sql statements in the .db file.
> I am using the SQLite Viewer extension offered in VS Code.

### Logging

```shell
import logging

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started") # add this at the beginning of the main method
logging.info("Program ended")  # add this at the end of the main method
```

### SQL Operations

> [1. create_tables.sql - create your database schema using sql](https://github.com/Bdowdle4/datafun-05-sql/blob/main/sql/create_tables.sql)
>
>[2. insert_records.sql - insert at least 10 additional records into each table.](https://github.com/Bdowdle4/datafun-05-sql/blob/main/sql/insert_records.sql)
>
>[3. update_records.sql - update 1 or more records in a table.](https://github.com/Bdowdle4/datafun-05-sql/blob/main/sql/update_records.sql)
>
>[4. delete_records.sql - delete 1 or more records from a table.](https://github.com/Bdowdle4/datafun-05-sql/blob/main/sql/delete_records.sql)
>
>[5. query_aggregation.sql - use aggregation functions including COUNT, AVG, SUM.](https://github.com/Bdowdle4/datafun-05-sql/blob/main/sql/query_aggregation.sql)
>
>[6. query_filter.sql - use WHERE to filter data based on conditions.](https://github.com/Bdowdle4/datafun-05-sql/blob/main/sql/query_filter.sql)
>
>[7. query_sorting.sql - use ORDER BY to sort data.](https://github.com/Bdowdle4/datafun-05-sql/blob/main/sql/query_aggregation.sql)
>
>[8. query_group_by.sql - use GROUP BY clause (and optionally with aggregation)](https://github.com/Bdowdle4/datafun-05-sql/blob/main/sql/query_group_by.sql)
>
>[9. query_join.sql - use INNER JOIN operation and optionally include LEFT JOIN, RIGHT JOIN, etc.](https://github.com/Bdowdle4/datafun-05-sql/blob/main/sql/query_join.sql)

### Python and SQL Integration

```shell
import sqlite3

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")
```

### Define Main Function for SQL Operations Script

```shell
def main():
    db_filepath = 'your_database.db'

    # Create database schema and populate with data
    execute_sql_from_file(db_filepath, 'insert_records.sql')
    execute_sql_from_file(db_filepath, 'update_records.sql')
    execute_sql_from_file(db_filepath, 'delete_records.sql')
    execute_sql_from_file(db_filepath, 'query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'query_filter.sql')
    execute_sql_from_file(db_filepath, 'query_sorting.sql')
    execute_sql_from_file(db_filepath, 'query_group_by.sql')
    execute_sql_from_file(db_filepath, 'query_join.sql')

    logging.info("All SQL operations completed successfully")
```

### Conditional Script Execution

```shell
if __name__ == "__main__":
    main()
```    