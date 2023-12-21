"""This script fetches the status from https://alu-intranet.hbtn.io/status"""
import requests
def fetch_status():
    """
    Fetches the status from https://alu-intranet.hbtn.io/status
    and displays information about the response body.
    """
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
if __name__ == "__main__":
    fetch_status()
