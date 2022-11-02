#!/usr/bin/python3
""" Returns the number of subscribers """
from sys import argv
from requests import get


def number_of_subscribers(subreddit):
    """ subscriptions of the channel """
    head = {'User-Agent': 'Chris Brown'}
    count = get('https://www.reddit.com/r/{}/about/json'.format(
        subreddit), headers=head).json()
    try:
        return count.get('data').get('subscribers')
    except:
        return 0


if __name__ == "__main__":
    number_of_subscribers(argv[1])
