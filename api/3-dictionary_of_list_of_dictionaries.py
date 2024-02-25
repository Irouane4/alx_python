import requests
import json

def get_employee_data(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    return employee_data

def get_employee_todos(employee_id):
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    return todos_data

def display_employee_todo_progress(employee_id):
    employee_data = get_employee_data(employee_id)
    employee_name = employee_data["name"]
    todos_data = get_employee_todos(employee_id)
    
    employee_tasks = []
    for task in todos_data:
        task_info = {
            "username": employee_name,
            "task": task["title"],
            "completed": task["completed"]
        }
        employee_tasks.append(task_info)
    
    return employee_tasks

if __name__ == "__main__":
    all_employees_tasks = {}
    
    for employee_id in range(1, 11):  # Assuming employee IDs range from 1 to 10
        employee_tasks = display_employee_todo_progress(employee_id)
        all_employees_tasks[str(employee_id)] = employee_tasks

    # Save data to JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_employees_tasks, json_file, indent=2)
