#!/usr/bin/python3
"""Script to send a POST request to a URL with an email parameter"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    response = requests.post(url, data={'email': email})
    print("Your email is: {}".format(response.text))
