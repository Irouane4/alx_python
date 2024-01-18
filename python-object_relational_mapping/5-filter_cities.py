import MySQLdb

# Connection
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user="user",
    password="password",
    db="hbtn_0e_4_usa",
    charset="utf8mb4"
)

# Function to fetch city names
def fetch_city_names(state_name):
    with db.cursor() as cursor:
        query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))
        result = cursor.fetchall()
        for row in result:
            print(row[0])

# Call the function
fetch_city_names("Arizona")
