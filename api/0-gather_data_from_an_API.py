"""
Module to gather data from a REST API and display employee TODO list progress.
"""

import requests
import sys

def get_employee_info(employee_id):
    """
    Get employee information from the specified REST API endpoint.
    
    Args:
        employee_id (int): The ID of the employee.
    
    Returns:
        dict: Employee information.
    """
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    return response.json()

def get_todo_list(employee_id):
    """
    Get TODO list information for the specified employee from the REST API endpoint.
    
    Args:
        employee_id (int): The ID of the employee.
    
    Returns:
        list: TODO list for the employee.
    """
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    return response.json()

def display_todo_progress(employee_id):
    """
    Display employee TODO list progress in the specified format.
    
    Args:
        employee_id (int): The ID of the employee.
    """
    employee_info = get_employee_info(employee_id)
    todo_list = get_todo_list(employee_id)

    employee_name = employee_info.get('name', 'Unknown')
    total_tasks = len(todo_list)
    done_tasks = [task['title'] for task in todo_list if task['completed']]
    
    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    
    for task_title in done_tasks:
        print(f"\t{task_title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Please provide a valid integer for the employee ID.")
        sys.exit(1)

    display_todo_progress(employee_id)
