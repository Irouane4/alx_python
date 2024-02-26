import csv
import requests
import sys

def get_employee_data(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)

    if employee_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Employee data not found.")
        return

    employee_data = employee_response.json()
    todos_data = todos_response.json()

    employee_name = employee_data['username']

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            task_completed_status = "True" if task['completed'] else "False"
            writer.writerow([employee_id, employee_name, task_completed_status, task['title']])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_data(employee_id)