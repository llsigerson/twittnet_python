
def userinfo_to_df(tweepy_output):
    """takes tweepy user info output and converts it to a handy dataframe"""

    def dictval_to_list(column,key):
        """takes a column of dictionaries and outputs a list of certain values in the dicts"""
        output= [entry[key] for entry in column]
        return output

    jsons= [json.loads(json.dumps(user._json)) for user in tweepy_output]
    df= pd.DataFrame(jsons)
    # set the indices to be the unique user ids
    df.index = df.id_str
    df.created_at = list(map(lambda x: datetime.datetime.strptime(x, "%a %b %d %H:%M:%S %z %Y"), df.created_at))

    return df

users = userinfo_to_df(api.lookup_users(screen_names=["jonfavs", "llsigerson"]))