#!/usr/bin/python3

"""
    Usage: <program> username password database state

    Finds the state 'state' from database
    Prevents SQL Injection
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(
        user=args[1], host='localhost', passwd=args[2], port=3306, db=args[3])
    cur = db.cursor()

    cur.execute(f'SELECT * FROM states WHERE name LIKE BINARY %s', (args[4], ))
    rows = cur.fetchall()

    for row in rows:
        print(row)
