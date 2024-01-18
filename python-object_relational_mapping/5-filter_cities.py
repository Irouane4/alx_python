import sys
import MySQLdb

def main():
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
        return

    username, password, database, state = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database)
    cursor = db.cursor()

    query = """
        SELECT c.name
        FROM cities c
        JOIN states s ON c.state_id = s.id
        WHERE s.name = %s
        ORDER BY c.id;
    """
    cursor.execute(query, (state,))
    cities = cursor.fetchall()

    db.close()

    if cities:
        print(", ".join(city[0] for city in cities))
    else:
        print("No cities found for '{}'".format(state))

if __name__ == "__main__":
    main()
