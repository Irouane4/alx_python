import sys
import csv
import requests

def get_employee_tasks(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch tasks for employee ID {employee_id}")
        sys.exit(1)

def export_to_csv(employee_id, tasks):
    file_name = f"{employee_id}.csv"
    with open(file_name, "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({"USER_ID": employee_id, "USERNAME": "Antonette", "TASK_COMPLETED_STATUS": task["completed"], "TASK_TITLE": task["title"]})

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    tasks = get_employee_tasks(employee_id)
    export_to_csv(employee_id, tasks)