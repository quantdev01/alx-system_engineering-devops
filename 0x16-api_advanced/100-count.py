#!/usr/bin/python3
"""
This module contains a recursive function to get hot article titles from a subr
and count the occurrences of given keywords.
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=''):
    """
    Recursively count keywords in hot article titles from a subreddit.
    """
    # Define the base URL for the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    # Define the headers for the request
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Define the parameters for pagination
    params = {'after': after} if after else {}

    # Make the GET request to the Reddit API
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

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
        return count_words(subreddit, word_list, hot_list, after)
    else:
        # When recursion is done, count the words
        word_count = {}

        # Normalize word_list to lowercase
        normalized_word_list = [word.lower() for word in word_list]

        for title in hot_list:
            words = title.lower().split()
            for word in words:
                if word in normalized_word_list:
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1

        # Filter out words with 0 count
        word_count = {k: v for k, v in word_count.items() if v > 0}

        # Sort by count descending, then alphabetically ascending
        sorted_word_count = sorted(
                word_count.items(), key=lambda item: (-item[1], item[0]))

        # Print the results
        for word, count in sorted_word_count:
            print(f"{word}: {count}")


# Example usage
if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming\
 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = [x for x in sys.argv[2].split()]
        count_words(subreddit, word_list)
