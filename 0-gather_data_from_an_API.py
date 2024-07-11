#!/usr/bin/python3
"""This is a flask implemantation"""

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/employe/<int:employee_id>')
def get_employee(employee_id):
    """ This functions returns employee id and returns 
    their todo list"""
    url = 'https://jsonplaceholder.typicode.com/todos/1'

    response = requests.get(url)
    data = response.json()
    employee_name = data.get('title')
    tasks = data.get('completed')
    
    data = {
        "employee_id": employee_id,
        "employee_name": employee_name,
        "tasks": tasks
    }

    return jsonify(data)

