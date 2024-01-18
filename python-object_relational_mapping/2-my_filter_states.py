#!/usr/bin/env python3

import sys
import MySQLdb

def filter_states(username, password, database, state_name):
    """Connects to a MySQL server and lists all states in the hbtn_0e_0_usa database with names matching the state_name argument."""

    db = MySQLdb.connect(user=username, passwd=password, db=database, host="localhost", port=3306)
    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    