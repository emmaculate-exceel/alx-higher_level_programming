#!/usr/bin/python3
import MySQLdb
from sys import argv
"""
class for MySQLdb
"""


def list_states(username, password, database):
    """
    function that creates a database
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    db.close()
