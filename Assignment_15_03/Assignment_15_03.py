# This application will read an iTunes export file in XML and produce a properly normalized database

import xml.etree.ElementTree as ET
import sqlite3


# Get the DB going
connection = sqlite3.connect('Track_DB.sqlite')
cursor = connection.cursor()
cursor.executescript('''
    CREATE TABLE IF NOT EXISTS Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS Genre (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE IF NOT EXISTS Track (
        id  INTEGER NOT NULL PRIMARY KEY
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id  INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );

''')

# Retrive XML file
fname = input('Enter file name : ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# Structure of xml
# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

# Function to retrive data from XML tree
def retrive(tree, value):
    found = False
    for node in tree:
        if found :
            return node.text
        if node.tag == 'key' and node.text == value :
            found = True
    return None

# Main Program
all_data = ET.parse(fname)
req_data = all_data.findall('dict/dict/dict')

# Get data from XML and insert in DB
for track in req_data :
    if retrive(track,'Track ID') is None:
        continue
    title = retrive(track,'Name')
    artist = retrive(track,'Artist')
    album = retrive(track,'Album')
    genre = retrive(track,'Genre')
    len = retrive(track,'Total Time')
    count = retrive(track,'Play Count')
    rating = retrive(track, 'Rating')

    # Check if main fields are empty
    if title is None or artist is None or album is None or genre is None :
        continue

    # Insert into DB

    # Artist
    cursor.execute('''INSERT OR IGNORE INTO Artist (name)
        VALUES ( ? )''', ( artist, ) )
    cursor.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cursor.fetchone()[0]

    # Album
    cursor.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
        VALUES ( ?, ? )''', ( album, artist_id ) )
    cursor.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cursor.fetchone()[0]

    # Genre
    cursor.execute('''INSERT OR IGNORE INTO Genre (name)
        VALUES ( ? )''', ( genre, ) )
    cursor.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cursor.fetchone()[0]

    # Track
    cursor.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, genre_id, len, rating, count)
        VALUES ( ?, ?, ?, ?, ?, ? )''',
        ( title, album_id, genre_id, len, rating, count ) )

    connection.commit()
