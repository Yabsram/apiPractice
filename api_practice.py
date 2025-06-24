import requests
import os

url = 'https://slack.com/api/'

response = requests.post(url + 'users.users.list', {'token': os.environ.get('SLACK_KEY')})

print(response.json())