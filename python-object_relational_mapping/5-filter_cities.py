#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a MySQL cursor
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = """
        SELECT GROUP_CONCAT(name ORDER BY id ASC SEPARATOR ', ')
        FROM cities
        WHERE state_id = (
            SELECT id FROM states WHERE name = %s
        )
    """

    # Execute the SQL query with the parameterized value
    cursor.execute(query, (state_name,))

    # Fetch the result
    result = cursor.fetchone()[0]

    # Display the result
    if result:
        print(result)

    # Close cursor and database connection
    cursor.close()
    db.close()
