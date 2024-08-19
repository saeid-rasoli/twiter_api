import tweepy
import json

with open("twitter_keys.json") as infile:
    json_obj = json.load(infile)
    bearer_token = json_obj["bearer_token"]
    access_token = json_obj["access_token"]
    access_token_secret = json_obj["access_token_secret"]
    api_key_secret = json_obj["api_key_secret"]
    api_key = json_obj["api_key"]

api = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
print('Authenticated...\n')

username = 'elonmusk'
user = api.get_user(username=username)
print('username:', user.data['name'])
print('id:', user.data['id'])
print(user)
