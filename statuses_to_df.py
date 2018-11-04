import re
import datetime
import pytz
def statuses_to_df(tweepy_output):
    """takes tweepy statuses output and converts it to a handy dataframe"""

    def dictval_to_list(column,key):
        """takes a column of dictionaries and outputs a list of certain values in the dicts"""
        output= [entry[key] for entry in column]
        return output

    jsons= [json.loads(json.dumps(status._json)) for status in tweepy_output]
    df= pd.DataFrame(jsons)
    #set the indices to be the unique tweet ids
    df.index= df.id_str

    #add in a few other helpful columns that are buried in dictionaries in tweepy
    df["user_id"]= dictval_to_list(df.user, "id_str")
    df["user_screen_name"] = dictval_to_list(df.user, "screen_name")

    #convert created_at column to datetime objects
    df.created_at = list(map(lambda x: datetime.datetime.strptime(x,  "%a %b %d %H:%M:%S %z %Y"), df.created_at))
    return df


tweets=statuses_to_df(api.user_timeline("jonfavs"))