#!/usr/bin/python3
"""
This is to print how many subs from Reddit username
"""
import requests


def number_of_subscribers(subreddit):
    """
    Number of suscribers getter function
    """
    # Getting the url
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # Setting the user-agent to use
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    try:
        # Getting the response
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except requests.RequestException:
        return 0
