#!/usr/bin/python3

"""
    Usage: <program> username password database

    Lists all cities in the database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(
        user=args[1], passwd=args[2], db=args[3], host='localhost')
    cur = db.cursor()
    cur.execute(""" SELECT cities.id, cities.name, states.name
                    FROM cities
                    LEFT JOIN states
                    ON states.id = cities.state_id
                    ORDER BY cities.id ASC
                """)
    rows = cur.fetchall()

    for row in rows:
        print(row)
