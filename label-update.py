import json
import sys
import requests

# Constants
REPO_OWNER = "brainhackorg"
REPO_NAME = "global2024"
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/labels"
TOKEN = sys.argv[1]
HEADERS = {
    "Authorization": f"token {TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# Read labels from JSON file
with open("labels.json", "r") as file:
    labels = json.load(file)


# Function to create or update a label
def create_or_update_label(label):
    response = requests.post(API_URL, headers=HEADERS, json=label)
    if response.status_code == 201:
        print(f"Created label: {label['name']}")
    elif response.status_code == 422:
        # Label already exists, update it
        update_url = f"{API_URL}/{label['name']}"
        response = requests.patch(update_url, headers=HEADERS, json=label)
        if response.status_code == 200:
            print(f"Updated label: {label['name']}")
        else:
            print(
                f"Failed to update label: {label['name']}, {response.status_code}, {response.text}"
            )
    else:
        print(
            f"Failed to create label: {label['name']}, {response.status_code}, {response.text}"
        )


# Upload labels to the repository
for label in labels:
    create_or_update_label(label)
