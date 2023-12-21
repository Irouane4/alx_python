#!/usr/bin/python3
"""This script sends a POST request with a letter as a parameter to a specified URL"""

import requests
import sys

def search_api(url, letter):
    """
    Sends a POST request to the specified URL with the 'q' parameter and displays the body of the response.

    Args:
        url (str): The URL to send the POST request to.
        letter (str): The letter to include in the request parameters.
    """
    payload = {'q': letter}

    response = requests.post(url, data=payload)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./5-json_api.py <URL> <letter>")
        sys.exit(1)

    url = sys.argv[1]
    letter = sys.argv[2]

    search_api(url.rstrip('/'), letter)
