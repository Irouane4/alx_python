import sys
import MySQLdb

def filter_cities(username, password, database, state):
    try:
        db = MySQLdb.connect(user=username, passwd=password, db=database, host="localhost", port=3306)
        cursor = db.cursor()

        query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state,))
        result = cursor.fetchall()

        if result:
            for row in result:
                print(row[0])
        else:
            print("No cities found in that state.")

    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> <database> <state>")
    else:
        filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])