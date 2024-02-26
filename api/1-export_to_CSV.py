import csv
import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users?id="
todos_url = "https://jsonplaceholder.typicode.com/todos"


def export_to_csv(id):
    """ Export user tasks to CSV """

    employee_url = f'https://jsonplaceholder.typicode.com/users/{id}'
    response = requests.get(employee_url)
    employee_data = response.json()

    todo_url = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    response = requests.get(todo_url)
    todo_data = response.json()

    filename = f'{id}.csv'

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                "USER_ID": id,
                "USERNAME": employee_data['name'],
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })

    print(f"{filename} created successfully.")
    

def user_info(id):
    """ Check user information """

    export_to_csv(id)

    total_tasks = 0
    response = requests.get(todos_url).json()
    for i in response:
        if i['userId'] == id:
            total_tasks += 1

    num_lines = 0
    with open(str(id) + ".csv", 'r') as f:
        for line in f:
            if not line == '\n':
                num_lines += 1

    if total_tasks == num_lines - 1:
        print("Number of tasks in CSV: OK")
    else:
        print("Number of tasks in CSV: Incorrect")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    user_info(int(sys.argv[1]))
