import requests
import sys


def post_email(url, email):
    # Define the payload with the email parameter
    payload = {'email': email}

    # Send a POST request to the specified URL with the payload
    response = requests.post(url, data=payload)

    # Display the email
    print("Your email is:", email)

    # Display the server's response
    print(response.text)


if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    # Extract the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Call the function to send the POST request and display the response
    post_email(url, email)
