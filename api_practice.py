import requests
import os

url = 'https://slack.com/api/conversations.join'

slack_token = os.environ.get('SLACK_KEY')

headers = {
    'Authorization': f'Bearer {slack_token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json={'channel': 'C092GGPJ8GP'})

print(response.json())
print()
print(response)