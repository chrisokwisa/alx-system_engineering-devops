#!/usr/bin/python3
""" contains a script that get the top ten subcribers """
from requests import get
from sys import argv


def top_ten(subreddit):
    """ top ten subscribers """
    head = {"User-Agent": 'abz'}
    try:
        count = get('https://www/reddit.com/r/{}hot.json?count=10'.format(
            subreddit), headers=head).json().get('data').get('children')
        print('\n'.join([dic.get('data').get('title')
                         for dic in output][:10]))
    except:
        print('None')


if __name__ == "__main__":
    top_ten(argv[1])
