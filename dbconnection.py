def get_database():
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb+srv://hesso:admin@hesso.q1q2q.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    #from pymongo import MongoClient
    client = pymongo.MongoClient(CONNECTION_STRING)

    # Create the database 
    return client['hesso']

