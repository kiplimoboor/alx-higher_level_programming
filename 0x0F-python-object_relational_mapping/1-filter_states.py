#!/usr/bin/python3

"""
    Lists all states with name starting with 'N'
    from table states in database hbtn_0e_0_usa

    Usage: <program> name password database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    args = sys.argv
    db = MySQLdb.connect(
        user=args[1], passwd=args[2], db=args[3], host='localhost', port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()

    for row in rows:
        print(row)
    
    cur.close()
    db.close()
