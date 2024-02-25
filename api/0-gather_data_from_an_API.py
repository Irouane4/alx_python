import requests
import sys

def get_employee_data(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    employee_response = requests.get(employee_url)
    todo_response = requests.get(todo_url)

    employee_data = employee_response.json()
    todo_data = todo_response.json()

    return employee_data, todo_data

def display_todo_progress(employee_data, todo_data):
    employee_name = employee_data.get('name')
    total_tasks = len(todo_data)
    completed_tasks = sum(task['completed'] for task in todo_data)
    completed_task_titles = [task['title'] for task in todo_data if task['completed']]

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for title in completed_task_titles:
        print(f"\t{title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data, todo_data = get_employee_data(employee_id)
    display_todo_progress(employee_data, todo_data)
    