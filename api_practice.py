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

userInfoURL = 'https://slack.com/api/users.list'

headers2 = {
    'Authorization': f'Bearer {slack_token}'
}

users_list_response = requests.get(userInfoURL, headers=headers2)
print(users_list_response.json())

print()

print(users_list_response)