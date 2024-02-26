import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"

def user_info(id):
    """ Check user information """
    total_tasks = 0
    response = requests.get(todos_url).json()
    for i in response:
        if i['userId'] == id:
            total_tasks += 1

    num_lines = 0
    try:
        with open(str(id) + ".csv", 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                num_lines += 1
    except FileNotFoundError:
        print("Number of tasks in CSV: Incorrect")
        return

    if total_tasks == num_lines - 1:  # Subtracting 1 to account for the header row
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <user_id>")
        sys.exit(1)

    user_info(int(sys.argv[1]))