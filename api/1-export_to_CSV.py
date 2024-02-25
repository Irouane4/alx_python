#!/usr/bin/python3
"""
Script to gather data from a REST API for a given employee ID and export to CSV.
"""

import csv
import requests
import sys

def get_employee_data(employee_id):
    """
    Get employee data from the API based on the employee ID.
    """
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    employee_response = requests.get(employee_url)
    todo_response = requests.get(todo_url)

    employee_data = employee_response.json()
    todo_data = todo_response.json()

    return employee_data, todo_data

def export_to_csv(employee_data, todo_data):
    """
    Export TODO list data to CSV.
    """
    employee_id = employee_data.get('id')
    employee_name = employee_data.get('username')
    filename = f"{employee_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            task_completed_status = str(task['completed'])
            task_title = task['title']
            csv_writer.writerow([str(employee_id), employee_name, task_completed_status, task_title])

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data, todo_data = get_employee_data(employee_id)
    export_to_csv(employee_data, todo_data)
