#!/usr/bin/env python3

import sys
import MySQLdb

def list_states(username, password, database):
    """Connects to a MySQL server and lists all states in the hbtn_0e_0_usa database."""

    db = MySQLdb.connect(user=username, passwd=password, db=database, host="localhost", port=3306)
    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
    