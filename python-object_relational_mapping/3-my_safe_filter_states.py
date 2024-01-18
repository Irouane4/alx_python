import sys
import MySQLdb

def filter_states(username, password, database, state_name):
    """Connects to a MySQL server and lists all states in the hbtn_0e_0_usa database with names matching the state_name argument, using a parameterized query to prevent SQL injection."""

    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database, host="localhost", port=3306)
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))
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
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <username> <password> <database> <state_name>")
    else:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
