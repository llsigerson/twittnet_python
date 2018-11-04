
import pytz
import datetime


def get_tweets(user, startday = datetime.datetime.utcnow().replace(tzinfo=pytz.utc)-datetime.timedelta(days=30), stopday= datetime.datetime.utcnow().replace(tzinfo=pytz.utc)):

    tweets= tweepy_to_df(api.user_timeline(user, count=200))
    #check if oldest tweet is still younger than our startday
    #while tweets.created_at[-1]>startday:

    return(tweets)

tweets=get_tweets("jonfavs")