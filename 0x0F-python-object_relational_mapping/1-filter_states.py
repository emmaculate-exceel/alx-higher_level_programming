#!/usr/bin/python3
"""
list all states in the database
which name starts with a capital N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host='localhost', port=3306, username=argv[1],
                                 password=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * state WHERE LIKE 'N%'")
    db_fetch = db_cursor.fetchall

    for row in db_fetch:
        print(row)
