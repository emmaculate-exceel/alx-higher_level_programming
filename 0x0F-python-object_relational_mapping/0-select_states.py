#!/usr/bin/python3
"""
class for MySQLdb
that list all states.id from the database
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    def list_states(username, password, database):
        """
        function that creates a database
        """
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=username, passwd=password, db=database)
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id")
        rows = cur.fetchall()

        for row in rows:
            print(row)
        cur.close()
        db.close()
