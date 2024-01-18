import sys
import mysql.connector
from mysql.connector import Error

def main():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3]
        )

        cursor = connection.cursor()
        query = "SELECT cities.id, cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (sys.argv[4],))
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print("{}: {}".format(row[0], row[1]))
        else:
            print("No cities found for that state.")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    main()
    