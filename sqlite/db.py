# Create table:
#   create table users(id INTEGER primary key, username TEXT, password TEXT);
# Insert
#   insert into users (username, password) values ('xpan', '123456');
# Tutorial
#   https://www.tutorialspoint.com/python_data_access/python_sqlite_create_table.htm

import sqlite3
import uuid

#Connecting to sqlite
conn = sqlite3.connect('example.db')

names = set()
with open('tmp.txt') as f:
    for line in f:
        line = line.strip()
        parts = line.split()
        for part in parts:
            part = part.strip()
            if len(part) == 0:
                continue
            if part.endswith('.'):
                continue
            names.add(part)

import uuid
data = {}
for name in names:
    data[name] = str(uuid.uuid4())

import json


with open('data.json', 'w') as outfile:
    json.dump(data, outfile)
