#!/usr/bin/python3
"""
Count the top ten article titles from hots
"""
import requests


def top_ten(subreddit):
    """
    Top ten articles priting
    """
    # we are retriving the url
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    # Defines header value
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Setting the limit request
    limit = {'limit': 10}

    # Make the get request to the Reddit API
    response = requests.get(
            url, headers=headers, params=limit, allow_redirects=False
            )

    if response.status_code == 200:
        # Catching for any error and return None
        try:
            # Gettin the data
            data = response.json()

            # for loop to print 10 titles article
            for i in range(10):
                print(data['data']['children'][i]['data']['title'])
        except Exception:
            print("None")
    else:
        print("None")
