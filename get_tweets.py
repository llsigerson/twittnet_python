import datetime
def get_tweets(user, startday = datetime.date.today()-datetime.timedelta(days=30), stopday= datetime.date.today()):
    tweets= tweepy_to_df(api.user_timeline(user))
    return(tweets)

tweets=get_tweets("jonfavs")