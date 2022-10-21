#!/usr/bin/python3
"""module that returns information about TODO list"""
import requests
from sys import argv

def todo(employeeID):
    """displays the employee TODO list in progress"""
    employee_name = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                employeeID)).json().get('employee')
    tasks = requests.get(
            'https://jsonplaceholder.typicode.com/{}/todos'.format(
                employeeID)).json()
    tasks_done = ['\t {}\n'.format(dic.get('title')) for dic in tasks
            if dic.get(completed)]
    if employee_name and tasks:
        print("Employee {} is done with tasks({}/{}:".format
            (employee_name, len(tasks_done), len(tasks)))
        print(''.join(task_done), end='')


if __name__ == "__main__":
    if len(argv) == 2:
        todo(int(argv[1]))
