#!/usr/bin/python3

"""
    Usage: <program> user password database state

    Lists all cities in a state
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv

    db = MySQLdb.connect(
        user=args[1], passwd=args[2], db=args[3], host='localhost')
    cur = db.cursor()

    cur.execute(""" SELECT name
                    FROM cities
                    WHERE state_id =
                        (SELECT id
                         FROM states
                         WHERE name = %s)
                """, (args[4], ))
    rows = cur.fetchall()
    rows = list(rows)
    rows = [row[0] for row in rows]

    print(*rows, sep=', ')

    cur.close()
    db.close()
