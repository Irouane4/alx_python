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

def get_employee_data(employee_id):
    # Get employee details
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(employee_url)
    employee_data = response.json()

    # Get employee TODO list
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(todo_url)
    todo_data = response.json()

    return employee_data, todo_data

def export_to_csv(employee_id, employee_name, todo_data):
    filename = f'{employee_id}.csv'

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for task in todo_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })

    print(f"{filename} created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data, todo_data = get_employee_data(employee_id)

    export_to_csv(employee_id, employee_data['name'], todo_data)
