#!/usr/bin/python3
"""Script to send a POST request to http://0.0.0.0:5000/search_user"""

import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    try:
        response = requests.post(url, data={'q': q})
        data = response.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
