#!/usr/bin/env python3
"""
Module to fetch and display TODO list progress for a given employee ID from the JSONPlaceholder API.
"""

import requests
import sys

def get_employee_data(employee_id):
    """
    Function to fetch employee data from JSONPlaceholder API.

    Parameters:
    - employee_id (int): Employee ID

    Returns:
    - dict: Employee data
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(url)
    return response.json()

def get_todo_list(employee_id):
    """
    Function to fetch TODO list for a given employee ID from JSONPlaceholder API.

    Parameters:
    - employee_id (int): Employee ID

    Returns:
    - list: TODO list
    """
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(url)
    return response.json()

def display_todo_progress(employee_id):
    """
    Function to display TODO list progress for a given employee ID.

    Parameters:
    - employee_id (int): Employee ID
    """
    employee_data = get_employee_data(employee_id)
    todo_list = get_todo_list(employee_id)

    employee_name = employee_data.get('name', 'Unknown Employee')
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task.get('completed'))

    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

    for task in todo_list:
        if task.get('completed'):
            print(f"\t{task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        display_todo_progress(employee_id)
    except ValueError:
        print("Please provide a valid integer for employee ID.")
        sys.exit(1)
