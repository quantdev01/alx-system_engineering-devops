#!/usr/bin/python3
"""
Getting the hot articles title using a recursive function
"""
import requests


# counter = 0
def recurse(subreddit, hot_list=[], after=''):
    """
    Recursive function
    """
    # Define the base URL for the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Define the headers for the request
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Define the parameters for pagination
    params = {'after': after}

    # Make the GET request to the Reddit API
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False
            )

    # Check if the request was successful
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json().get('data', {})

    # Get the list of hot articles
    children = data.get('children', [])

    # Add the titles of the hot articles to the hot_list
    for child in children:
        hot_list.append(child['data']['title'])

    # Check if there are more pages to fetch
    after = data.get('after')
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
