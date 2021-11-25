import tweepy
import datetime

#Date checking and formating
today = datetime.datetime.now()
date_formated = today.strftime("%d/%m/%Y")


# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object and test Authentication
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# Post a tweet
api.update_status("Today " + str(date_formated) + " everything is good")