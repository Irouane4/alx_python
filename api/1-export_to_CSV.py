import sys
import csv

def get_employee_data(employee_id):
    # Replace this with your actual API call to get employee data
    employee_data = {
        "id": employee_id,
        "name": f"Employee {employee_id}",
    }
    return employee_data

def get_employee_todos(employee_id):
    # Replace this with your actual API call to get employee tasks
    todos_data = [
        {"id": 1, "title": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": False},
        {"id": 2, "title": "distinctio vitae autem nihil ut molestias quo", "completed": True},
        {"id": 3, "title": "et itaque necessitatibus maxime molestiae qui quas velit", "completed": False},
        {"id": 4, "title": "adipisci non ad dicta qui amet quaerat doloribus ea", "completed": False},
        {"id": 5, "title": "voluptas quo tenetur perspiciatis explicabo natus", "completed": True},
        {"id": 6, "title": "aliquam aut quasi", "completed": True},
        {"id": 7, "title": "veritatis pariatur delectus", "completed": True},
        {"id": 8, "title": "nesciunt totam sit blanditiis sit", "completed": False},
        {"id": 9, "title": "laborum aut in quam", "completed": False},
        {"id": 10, "title": "nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis", "completed": True},
        {"id": 11, "title": "sunt cum tempora", "completed": False},
        {"id": 12, "title": "totam quia non", "completed": True},
        {"id": 13, "title": "sint sit aut vero", "completed": False},
        {"id": 14, "title": "porro aut necessitatibus eaque distinctio", "completed": False},
    ]
    return todos_data

def export_employee_todos_to_csv(employee_id):
    employee_data = get_employee_data(employee_id)
    employee_name = employee_data["name"]
    todos_data = get_employee_todos(employee_id)
    done_tasks = [todo for todo in todos_data if todo["completed"]]
    total_tasks = len(todos_data)
    done_tasks_count = len(done_tasks)
    print(f"Employee {employee_name} is done with tasks({done_tasks_count}/{total_tasks}):")
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in todos_data:
            writer.writerow({"USER_ID": employee_id, "USERNAME": employee_name, "TASK_COMPLETED_STATUS": task["completed"], "TASK_TITLE": task["title"]})

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_employee_todos_to_csv(employee_id)
    