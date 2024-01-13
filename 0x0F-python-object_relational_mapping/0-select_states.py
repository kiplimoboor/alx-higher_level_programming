#!/usr/bin/python3

""" This module simply connects to the hbtn_0e_0_usa
    database, and gets data from the states table.

    It uses the localhost

    Usage: <program> user password database
"""

import MySQLdb
import sys

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
