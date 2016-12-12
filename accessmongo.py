from pymongo import MongoClient

def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):
    """ Get named database from MongoDB with/out authentication """
    # make Mongo connection with/out authentication
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s' % (username,password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
       conn = MongoClient(host,port)

    return conn[db_name]
