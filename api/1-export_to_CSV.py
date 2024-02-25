#!/usr/bin/env python3

"""
Module documentation goes here.
"""

import csv
import sys
import requests

def get_employee_data(employee_id):
    """
    Function documentation goes here.
    """
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    employee_response = requests.get(employee_url)
    todo_response = requests.get(todo_url)

    employee_data = employee_response.json()
    todo_data = todo_response.json()

    return employee_data, todo_data

def export_to_csv(employee_id, employee_name, todo_data):
    """
    Function documentation goes here.
    """
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in todo_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": str(task["completed"]),
                "TASK_TITLE": task["title"]
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_data, todo_data = get_employee_data(employee_id)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

    employee_name = employee_data["username"]
    completed_tasks = sum(task["completed"] for task in todo_data)
    total_tasks = len(todo_data)

    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todo_data:
        if task["completed"]:
            print(f"\t{task['title']}")

    export_to_csv(employee_id, employee_name, todo_data)
