#!/usr/bin/python3
"""
Count the top ten article titles from hots
"""
import requests


def top_ten(subreddit):
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MyRedditBot/1.0'}
    limit = {'limit': 10}
    response = requests.get(url, headers=headers, params=limit)

    try:
        data = response.json()
        for i in range(10):
            print(data['data']['children'][i]['data']['title'])
    except Exception:
        print("None")
