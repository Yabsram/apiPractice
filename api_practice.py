import requests
import os
import pandas as pd
import sqlalchemy as db

url = 'https://slack.com/api/conversations.join'

slack_token = os.environ.get('SLACK_KEY')

headers = {
    'Authorization': f'Bearer {slack_token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json={'channel': 'C092GGPJ8GP'})

userInfoURL = 'https://slack.com/api/users.list'

headers2 = {
    'Authorization': f'Bearer {slack_token}'
}

users_list_response = requests.get(userInfoURL, headers=headers2)
print(users_list_response.json())


df = pd.DataFrame.from_dict(users_list_response)
print(df)
'''

engine = db.create_engine('sqlite:///users.db')

df.to_sql('slackUsers', con=engine, if_exists='replace', index=False)

with engine.connect() as connection:
   query_result = connection.execute(db.text("SELECT * FROM slackUsers;")).fetchall()
   print(pd.DataFrame(query_result))
   '''