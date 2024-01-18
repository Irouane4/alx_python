"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cur = db.cursor()

    # Execute SQL query to retrieve states starting with 'N'
    query = """
        SELECT * FROM states
        WHERE name LIKE 'N%'
        ORDER BY id ASC
    """
    cur.execute(query)

    # Fetch all rows and print the result
    states = cur.fetchall()
    for state in states:
        print(state)

    # Close cursor and database connection
    cur.close()
    db.close()
