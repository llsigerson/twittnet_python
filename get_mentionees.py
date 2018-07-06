
def get_mentionees(tweets):
    mentionees= dict()
    for entities in tweets["entities"]:
        #get all users mentioned in the tweet
        if len(entities["user_mentions"])>0:
            names = [entry["id_str"] for entry in entities["user_mentions"]]
            #update the mentionees dictionary with these names
            for name in names:
                if name in mentionees.keys():
                    mentionees[name]+=1
                else:
                    mentionees[name]=1
    return (mentionees)

