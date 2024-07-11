import requests
from sys import argv

def get_employee_todos(employee_id):
    """Stuff"""
    
    site = "https://jsonplaceholder.typicode.com/"
    user = requests.get(site + "users/{}".format(employee_id))
    todos = requests.get(site + "todos?userId={}".format(employee_id))
    print(site, user, todos)


if __name__ == "__main__":
    get_employee_todos(employee_id=argv[1])
