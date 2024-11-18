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
    todos = requests.get(todo, params={"userId": user}).json()

    complete_todo = [t["title"] for t in todos if t["completed"]]
    total_todos = len(todos)
    done = len(complete_todo)

    print (
        f"\nEmployee {usernames} is done with tasks({done}/{total_todos}):"
    )

    for dos in complete_todo:
        print("\t{}".format(dos))


if __name__ == "__main__":
    get_employee_todos(employee_id=argv[1])

