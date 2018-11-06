import flatten_dict as fd
import pandas as pd
def ratelimit_to_df(authentication):
    #load in data as a dictionary of dictionaries
    init_data= json.loads(json.dumps(authentication.rate_limit_status()))
    #flatten to a single dictionary with a tuple for each key
    init_data= fd.flatten(d=init_data["resources"], reducer="tuple")
    #create a list of the keys (tuples) for easy iteration later
    key_list = list(init_data.keys())

    #initialize empty dataframe that'll be added to iteratively row by row
    data= pd.DataFrame({"Type":[],"Resource":[], "Limit": [], "Remaining":[], "Reset":[]})
    #build the dataframe
    for key in key_list:
        if key[2]== "limit":
            data=data.append({"Type": key[0] ,"Resource": key[1], "Limit": init_data[key], "Remaining":np.nan,
                          "Reset":np.nan}, ignore_index=True)
        elif key[2] == "remaining":
            data.loc[data.Resource==key[1],"Remaining"]= init_data[key]
        elif key[2] == "reset":
            data.loc[data.Resource == key[1], "Reset"] = init_data[key]
    #add a logical column just to indicate whether the resource has been used at all
    data["Used"]= data.Limit>data.Remaining
    return data

test= ratelimit_to_df(api)
