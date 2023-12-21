import requests
import sys

def post_email(url, email):
    payload = {'email': email}
    response = requests.post(url, data=payload)
    if "Email:" in response.text:
        email_part = response.text.split("Email:")[1].strip()
        print("Email:", email_part)
    else:
        print("Server response did not contain expected format.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
