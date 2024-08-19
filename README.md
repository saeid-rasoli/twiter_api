# twiter_api
twitter (x) crawler using tweepy and and fastapi with twitter (x) api

in this simple project we add username to the endpoint and get the username, name and id of the user and pass as json file

for fetching data we use tweepy and for using this method we use twitter (x) api free version for this purpose

**NOTE**

all before twitter api features such as fetching tweets, get all tweets infos such as number of likes, retweets, shares and ..., has been gone on free edition, and all of these features will work only on paid edition.

**Examples:**

endpoint /
```json
{
  "message": "welcome, please append username to the url to get user info, and don't forget to active proxy"
}
```

endpoint /username
```json
{
  "name": "Elon Musk",
  "id": 44196397,
  "username": "elonmusk"
}
```