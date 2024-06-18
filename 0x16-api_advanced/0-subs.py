#!/usr/bin/python3
"""
This is to print how many subs from Reddit username
"""
import requests


def number_of_subscribers(subreddit):
    """
    Number of suscribers getter function
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        subscribers = data['data']['subscribers']

        return subscribers
    else:
        return 0
