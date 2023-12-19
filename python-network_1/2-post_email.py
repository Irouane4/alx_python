#!/usr/bin/python3
"""This script sends a POST request with an email parameter to a specified URL"""

import requests
import sys
from urllib.parse import urlencode


def post_email(url, email):
    """
    Sends a POST request with an email parameter to the specified URL
    and displays the body of the response.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include in the URL parameters.
    """
    params = urlencode({'email': email})

    # Ensure proper URL formatting
    if not url.endswith('/'):
        url += '/'

    full_url = f"{url}post_email?{params}"

    response = requests.post(full_url)

    print(f"Your email is: {email}")
    print(response.text)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url.rstrip('/'), email)
