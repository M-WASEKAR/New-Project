# 5. Provide a program to create tables (Employee, Department, Project) in database Sqlite and insert the data.


import sqlite3


def sql_connection():
    conn = sqlite3.connect("mydatabase.db")
    return conn


def sql_table(conn):
    cursorObj = conn.cursor()
    # Create the table
    cursorObj.execute(
        "CREATE TABLE Employee(e_name varchar(30), dept varchar(35), project varchar(35));"
    )
    cursorObj.execute("CREATE TABLE Department (D_name varchar(20), ")
    cursorObj.execute("CREATE TABLE Project (P_no varchar(10), p_name varchar(30)")
    # Insert records
    cursorObj.executescript(
        """
   INSERT INTO Employee VALUES('Jay', 'production', 'sales');
   INSERT INTO Department VALUES('production);
   INSERT INTO Project VALUES(2,'sales');
   """
    )
    conn.commit()
    cursorObj.execute("SELECT * FROM Employee")
    rows = cursorObj.fetchall()
    print("details:")
    for row in rows:
        print(row)


sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if sqllite_conn:
    sqllite_conn.close()
    print("\nThe SQLite connection is closed.")
