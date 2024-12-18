#!/usr/bin/python3
"""This was a doozy"""
import json
import requests
from sys import argv


def get_employee_todos(employee_id):
    """Stuff"""

    site = "https://jsonplaceholder.typicode.com/"
    user = site + "users/{}".format(employee_id)
    todo = site + "todos/"

    users = requests.get(user).json()
    usernames = users['name']
    todos = requests.get(todo, params={'userId': employee_id}).json()

    complete_todo = [t["title"] for t in todos if t["completed"]]
    total_todos = len(todos)
    done = len(complete_todo)

    progress_message = (
        f"\nEmployee {usernames} is done with tasks({done}/{total_todos}):"
    )

    completed_task_titles = [
        f"\t{todo}"
        for todo in complete_todo
    ]

    print(progress_message)
    print("\n".join(completed_task_titles))


if __name__ == "__main__":
    get_employee_todos(employee_id=argv[1])
