# This application will read the mailbox data (mbox.txt)
# and count the number of email messages per organization
# (i.e. domain name of the email address) using a database

import sqlite3

# Set connection to DB
connection = sqlite3.connect('Email_DB.sqlite')
cursor = connection.cursor()

# Create fresh table
cursor.execute('''
        DROP TABLE IF EXISTS Counts
    ''')

cursor.execute('''
        CREATE TABLE Counts (
            org TEXT, count INTEGER
        )
    ''')

# Process .txt file to DB
fname = input('Enter the file name : ')
if len(fname) < 1:
    fname = 'mbox.txt'
fhandle = open(fname)

for line in fhandle:
    if not line.startswith('From: '):
        continue
    organization = line.rstrip().split('@')[1]

    # Check if the record already exits
    cursor.execute('SELECT COUNT FROM COUNTS WHERE ORG = ?', (organization,))
    row = cursor.fetchone()

    # Record not found
    if row is None:
        cursor.execute('INSERT INTO COUNTS (ORG, COUNT) VALUES(?, 1)', (organization,))

    # Record found
    else:
        cursor.execute('UPDATE COUNTS SET COUNT = COUNT + 1 WHERE ORG = ?', (organization,))

connection.commit()

# Retrieve data
sql_query = 'SELECT * FROM COUNTS ORDER BY COUNT DESC LIMIT 10'

for row in cursor.execute(sql_query):
    print(row[0], row[1])

cursor.close()
