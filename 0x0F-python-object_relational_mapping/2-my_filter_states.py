#!/usr/bin/python3

"""
    Usage: <program> name password database state

    Finds state from arguments
    from table states in database hbtn_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(host='localhost', user=args[1],
                         passwd=args[2], db=args[3], port=3306)
    cur = db.cursor()
    cur.execute(f'SELECT * FROM states WHERE name = "{args[4]}"')
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()