#!/usr/bin/python3
"""export to CSV"""
import csv
from requests import get
from sys import argv


def csvWrite(user):
    """get the csv"""
    data = get('https://jsonplaceholder.typicode.com/tools?serId={}'.format(
        user)).json()
    name = get('https://jsonplaceholder.typicode.com/users/{}'.format(
        user)).json().get('username')
    employ_data = open('{}.csv'.format(user), 'w')
    cwrite = csv.writer(employ_data, quoting=csv.QUOTE_ALL)
    for line in data:
        lined = [line.get('userId'), name,
                 line.get('completed'), line.get('title')]
        cwrite.writerow(lined)
    employ_data.close()


if __name__ == "__main__":
    csvWrite(argv[1])
