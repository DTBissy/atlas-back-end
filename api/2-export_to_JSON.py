#!/usr/bin/python3
"""This was a doozy"""
import requests
import json
from sys import argv


def get_employee_todos(employee_id):
    """Stuff"""

    site = "https://jsonplaceholder.typicode.com/"
    user = requests.get(site + "users/{}".format(employee_id))
    todo = requests.get(site + "todos?userId={}".format(employee_id))

    users = user.json()
    usernames = users.get("username")
    todos = todo.json()

    # print(site, todos, usernames)

    completed = [i for i in todos if i.get("completed")]

    data = {employee_id: [{
        "task": i.get("title"),
        "completed": i.get("completed"),
        "username": usernames
        } for i in completed]}

    formatted = json.dumps({str(employee_id): data})

    with open("{}.json".format(employee_id), "w") as f:
        f.write(formatted)
        f.close()


if __name__ == "__main__":
    get_employee_todos(employee_id=argv[1])
