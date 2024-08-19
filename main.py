from fastapi import FastAPI
import tweepy
import json

app = FastAPI()


@app.get("/")
async def root():
    message = "welcome, please append username to the url to get user info, and don't forget to active proxy"
    return {"message": message}


@app.get("/{username}")
async def get_usename_data(username: str):
    with open("twitter_keys.json") as infile:
        json_obj = json.load(infile)
        bearer_token = json_obj["bearer_token"]

    api = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)
    print("Authenticated...\n")

    user = api.get_user(username=username)
    get_name = user.data["name"]
    get_id = user.data["id"]
    get_username = user.data["username"]
    return {"name": get_name, "id": get_id, "username": get_username}
