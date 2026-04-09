import sqlite3 as sql

#create a connection to connect to a database
connection = sql.connect("gym.db")
#create a cursor to connect to schema
cursor = connection.cursor()
# open the schema file
with open("schema.sql", "r") as file:
    sql_script = file.read()

# execute all SQL commands inside schema.sql
cursor.executescript(sql_script)

# save changes
connection.commit()

# close connection
connection.close()