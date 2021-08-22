def get_database():
    import pymongo
    from dotenv import load_dotenv
    import os
    
    load_dotenv()
    DBpassword = os.environ['DB_PASSWORD']

    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    CONNECTION_STRING = f'mongodb+srv://MDOuser:{DBpassword}@mdo-cluster-01.g6jsh.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = pymongo.MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['MDO']
    
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":    
    
    # Get the database
    dbname = get_database()
    aircrafts = dbname["aircrafts"]

    item_details = aircrafts.find()
    from pandas import DataFrame
    items_df = DataFrame(item_details)
    print(items_df)