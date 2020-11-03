# Create table:
#   create table users(id INTEGER primary key, username TEXT, password TEXT);
# Insert
#   insert into users (username, password) values ('xpan', '123456');
# Tutorial
#   https://www.tutorialspoint.com/python_data_access/python_sqlite_create_table.htm

import sqlite3

#Connecting to sqlite
conn = sqlite3.connect('example.db')
