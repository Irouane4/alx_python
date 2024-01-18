#!/usr/bin/env python3

import sys
import MySQLdb

def list_cities(username, password, database):
    """Connects to a MySQL server and lists all cities from the hbtn_0e_4_usa database, sorted by cities.id, with only one execute() call."""

    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database, host="localhost", port=3306)
        cursor = db.cursor()
        query = "SELECT * FROM cities ORDER BY cities.id ASC"
        cursor.execute(query)
        result = cursor.fetchall()

        for row in result:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-my_cities.py <username> <password> <database>")
    else:
        list_cities(sys.argv[1], sys.argv[2], sys.argv[3])