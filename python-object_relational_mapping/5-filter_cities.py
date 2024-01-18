import pymysql

# Connection
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='user',
    password='password',
    db='test_5',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Function to fetch city names
def fetch_city_names(state_name):
    with conn.cursor() as cursor:
        query = "SELECT cities.id, cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))
        result = cursor.fetchall()
        return result

# Call the function
cities = fetch_city_names("Arizona")
for city in cities:
    print(city['name'])
    