
import format_backend

'''

from pymongo import MongoClient

def print_tweets_collection_info():
    # Connect to the MongoDB server running on localhost at port 27017
    

    # Select the '291db' database
    db = client['291db']

    # Select the 'tweets' collection within the '291db' database
    tweets_collection = db['tweets']

    # Print information about the 'tweets' collection
    print("Information about the 'tweets' collection:")
    print(f"Database: {db.name}")
    print(f"Collection: {tweets_collection.name}")
    print(f"Number of documents: {tweets_collection.count_documents({})}")

    # Close the MongoDB connection
    client.close()

# Example usage
print_tweets_collection_info()
'''



from pymongo import MongoClient
from pprint import pprint

def get_tweets_by_keywords(database_name, collection_name, keywords):
    # Connect to the MongoDB server running on localhost at port 27017
    client = MongoClient('mongodb://localhost:27017/')

    # Access the specified database
    db = client[database_name]

    # Access the specified collection in the database
    collection = db[collection_name]

    # Build a query to find tweets with the specified keywords in the 'content' field
    key_query = []
    for i in keywords:
        a_holder = {'content': {'$regex': str(i), "$options": "i"}}
        key_query.append(a_holder)




    query = {
    '$and': key_query
    }
    

    # Query the collection
    results = list(collection.find(query))


    # Close the MongoDB connection
    client.close()

    # Return the results
    return results

# Example usage:
database_name = '291db'
collection_name = 'tweets'
keywords = ['suPPort', 'FarmersProtest', 'coUNTry']

tweets_with_keywords = get_tweets_by_keywords(database_name, collection_name, keywords)

# Print the results
print(f"Tweets containing all keywords {keywords}:")
for tweet in tweets_with_keywords:

    pprint(tweet)

    #a_id,date,content,username = format_backend.info_tweet(tweet)
    #print(a_id)
    #print(date)
    #print(content)
    #print(username)

    #username, display_name, location = format_backend.info_userLocation(tweet)
    #print(username)
    #print(display_name)
    #print(location)

    #pprint(format_backend.json_user(tweet))

    #username, display_name, follower_count = format_backend.info_userfollowersCount(tweet)
    #print(username)
    #print(display_name)
    #print(follower_count)

# db.tweets.find({content: {$all: [Support, FarmersProtest]}})
# db.tweets.find({content: {$regex: "support"}})