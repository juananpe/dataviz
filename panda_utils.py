from accessmongo import *
import pandas as pd

def mongo_to_dataframe(db_name, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=True):
    """ create a dataframe from mongodb collection """

    db = get_mongo_database(db_name, host, port, username, password)
    cursor = db[collection].find(query)
    df = pd.DataFrame(list(cursor))
    if no_id:
        del df['_id']

    return df


def dataframe_to_mongo(df, db_name, collection, host='localhost', port=27017, username=None, password=None):
    """ save a dataframe to mongodb collection """
    db = get_mongo_database(db_name, host, port, username, password)
    records = df.to_dict('records')
    db[collection].insert(records)


