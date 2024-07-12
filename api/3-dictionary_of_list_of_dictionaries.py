#!/usr/bin/python3
"""This script collects tasks from all employees and exports them in JSON format."""
import json
import requests
from sys import argv


def get_all_employee_todos():
    """Fetches and organizes todos for all employees."""
    site = "https://jsonplaceholder.typicode.com/"

    site = "https://jsonplaceholder.typicode.com/"
    # Fetch all users
    users_response = requests.get(site + "users")
    users = users_response.json()

    # Initialize an empty dictionary to hold all tasks
    all_tasks = {}

    # Iterate through each user
    for user in users:
        user_id = user['id']
        username = user['username']

        # Fetch todos for the current user
        todos_response = requests.get(site + "todos?userId={}".format(user_id))
        todos = todos_response.json()

        # Organize todos under the user's ID in the all_tasks dictionary
        all_tasks[user_id] = [{"username": username, "task": i.get('title'), "completed": i.get('completed')} for i in todos]
    
    return all_tasks


def save_to_json(all_tasks):
    """Saves the collected tasks to a JSON file."""
    filename = "todo_all_employees.json"
    with open(filename, "w") as file:
        json.dump(all_tasks, file)

if __name__ == "__main__":
    all_tasks = get_all_employee_todos()
    save_to_json(all_tasks)
