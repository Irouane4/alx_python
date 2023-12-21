"""This script sends a request to a URL and displays the body of the response.
Prints an error message if the HTTP status code is greater than or equal to 400.
"""
import requests
import sys

def fetch_url(url):
    """
    Sends a request to the specified URL and displays the body of the response.
    Prints an error message if the HTTP status code is greater than or equal to 400.

    Args:
        url (str): The URL to send the request to.
    """
    response = requests.get(url)

    print(response.text)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./4-error_code.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url(url)
