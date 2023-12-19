"""This script sends a request to a URL and displays the value of the variable X-Request-Id in the response header"""

import requests
import sys


def fetch_x_request_id(url):
    """
    Sends a request to the specified URL and displays the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request to.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    print(x_request_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
