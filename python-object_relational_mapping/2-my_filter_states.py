#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Execute SQL query to retrieve states with the specified name
    query = """
        SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC
    """
    cur.execute(query, (state_name,))

    # Fetch all rows and print the result
    states = cur.fetchall()
    for state in states:
        print(state)

    # Close cursor and database connection
    cur.close()
    db.close()
