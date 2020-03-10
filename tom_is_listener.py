import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("MIjdhsGgxXDf6x42njMNoUGcp", "diqNByAalW57PxaHzHVeTZXVhWlLwOwtVtaKxz8ooaTFWqfG61")
auth.set_access_token("1237176395740196865-VJGXrPrbyWEHTSeHNQivI0VOD1zabo", "gZrIXk5Ijy7W3kjgpiVUeHaGELIk1QTcOMDGJPfVeXcXs")

# Create API object
api = tweepy.API(auth)

# Create a tweet
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['@tom_is_alone', '@tomisalone2'])