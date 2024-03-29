#!/usr/bin/python3
""" Returns the list containing titles of all hot articles for subreddit """
from requests import get
from sys import argv


def recurse(subreddit, hotlist=[], after=None):
    """ subscribers """
    head = {'User-Agent': 'Chris Brown'}
    try:
        if after:
            count = get('https://www.reddit.com/r/{}/hot.json?after={}'.format(
                subreddit, after), headers=head).json().get('data')
        else:
            count = get('https://www/reddit.com/r/{}/hot.json'.format(
                subreddit), headers=head).json().get('data')
        hotlist += [dic.get('data').get('title')
                    for dic in count.get('children')]
        if count.get('after'):
            return recurse(subreddit, hotlist, after=count.get('after'))
        return hotlist
    except:
        return None


if __name__ == "__main__":
    recurse(argv[1])
