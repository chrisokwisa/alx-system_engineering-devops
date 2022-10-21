#!/usr/bin/python3
"""gets api"""
import requests
from sys import argv


def todo(userid):
    """Gets all information about employees progress in tasks done"""
    employee_name = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
            userid)).json().get('name')
    number_of_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
            userid)).json()
    tasks_done = ['\t {}\n'.format(dic.get('title')) for dic in number_of_tasks
                 if dic.get('completed')]
    if employee_name and number_of_tasks:
        print("Employee {} is done with tasks({}/{}):".format
              (employee_name, len(tasks_done), len(number_of_tasks)))
        print(''.join(tasks_done), end='')


if __name__ == "__main__":
    if len(argv) == 2:
        todo(int(argv[1]))
