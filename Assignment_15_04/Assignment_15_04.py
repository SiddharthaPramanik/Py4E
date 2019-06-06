# This application will read roster data in JSON format, parse the file, and
# then produce an SQLite database that contains a User, Course, and Member table
# and populate the tables from the data file.

import json
import sqlite3

# DB Setup
connection = sqlite3.connect('Roster_DB.sqlite')
cursor = connection.cursor()
cursor.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Get the JSON file
fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

# JSON File, data foramt
# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

# Retrive data from JSON and populate DB
str_data = open(fname).read()
json_data = json.loads(str_data)

for data_block in json_data:

    name = data_block[0]
    title = data_block[1]
    role = data_block[2]

    # User Table
    cursor.execute('''INSERT OR IGNORE INTO User (name)
        VALUES ( ? )''', ( name, ) )
    cursor.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cursor.fetchone()[0]

    # Course Table
    cursor.execute('''INSERT OR IGNORE INTO Course (title)
        VALUES ( ? )''', ( title, ) )
    cursor.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cursor.fetchone()[0]

    # Member Table
    cursor.execute('''INSERT OR REPLACE INTO Member
        (user_id, course_id, role) VALUES ( ?, ?, ? )''',
        ( user_id, course_id, role ) )

    connection.commit()
