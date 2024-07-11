#!/usr/bin/python3
"""This was a doozy"""
import requests
import csv
from sys import argv


def get_employee_todos(employee_id):
    """Stuff"""

    site = "https://jsonplaceholder.typicode.com/"
    user = requests.get(site + "users/{}".format(employee_id))
    todo = requests.get(site + "todos?userId={}".format(employee_id))

    users = user.json()
    usernames = users.get("username")
    todos = todo.json()
    csv_file_name = "{}.csv".format(employee_id)
    # print(site, users, todos, names)

    completed = [i for i in todos if i.get("completed")]

    # print("Employee {} is done with tasks({}/{}):"
    #       .format(names, done_todos, all_todos))

    for i in completed:
        print("\t {}".format(i.get("title")))

    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for i in todos:
            writer.writerow([i.get('userId'), i.get('title'),
                             i.get('completed')])


if __name__ == "__main__":
    get_employee_todos(employee_id=argv[1])
