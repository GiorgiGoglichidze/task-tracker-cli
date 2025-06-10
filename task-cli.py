import os
import sys
import json
from datetime import datetime


tasks = []

if os.path.exists("tasks.json"):
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        tasks = []
else:
    tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_funciton(description):
    date_create = datetime.now().isoformat()
    status = "todo"
    ID = len(tasks) + 1
    date_update =  "-"

    tasks.append({"id":ID,
                  "description":description,
                  "status":status,
                  "createdAt": date_create,
                  "updatedAt":date_update})
    
    save_tasks()

    return ID

def update_function(ID,description):
    task = tasks[ID-1]
    task["description"] = description
    task["updatedAt"] = datetime.now().isoformat()
    
    save_tasks()

def delete_function(ID):
    if 0 >=  ID  or ID >len(tasks):
        print("Please Enter A valid ID")
        return
    tasks.pop(ID-1)

    for i, task in enumerate(tasks):
        task["id"] = i + 1


    save_tasks()

def list_tasks(status = None):
    
    for task in tasks:
        if (status is None) or (task["status"] == status):
            ID = task["id"]
            description = task["description"]
            date_created = task["createdAt"]
            date_updated = task["updatedAt"]
            task_status =  task["status"]
            print(f"[{ID}]| {description} | Status: {task_status} | Created: {date_created} | Updated: {date_updated}")




commands = ["add","delete","update","mark-in-progress","mark-done","list"]
command = ""
if len(sys.argv) > 1 and sys.argv[1].lower() in commands:
    command = sys.argv[1].lower()
else:
    print('Please Enter A valid command') 
    sys.exit(1)





if command == "add":
    description = sys.argv[2]
    ID = int(add_funciton(description))
    print(f"Task added succesfully (ID: {ID})")

elif command == "update":

    if len(sys.argv) < 4:
        print("Please Enter by format: update <ID>  <description>")
    else:
        try:
            ID = int(sys.argv[2])
        except ValueError:
            print("ID must be a number")
            sys.exit(1)
    description = sys.argv[3]
    update_function(ID,description)

elif command == "delete":
    if len(sys.argv < 3):
        print("Please Enter by format: delete <ID>")           

    try:
        ID = int(sys.argv[2])
    except ValueError:
        print("ID must be a number")
        sys.exit(1)   
    delete_function(ID)

elif command == "list":

    if len(sys.argv) > 2:
        second_command = sys.argv[2]
        if second_command.lower() not in ["done","todo","in-progress"]:
            print("Invalid Status,please enter Valid status to list.")
        else:
            list_tasks(second_command)
    else:
        list_tasks()
