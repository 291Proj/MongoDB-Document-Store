from datetime import datetime
from pymongo import MongoClient

# Global variables
client = None
db = None
tweets_collection = None

def connect_dbserver(port: str) -> None:
    '''
    Establishes a Connection to the mongodb server
    Parameters:
        -port: '27017'
    Returns:
        -N/A
    '''
    global client, db, tweets_collection
    client = MongoClient(f'mongodb://localhost:{port}/') #connects through port
    db = client["291db"]  # Create or open the video_store database on server.
    tweets_collection = db["tweets"] # Create or open the collection in the db


def connect_close() -> None:
    '''
    Closes the connection to the mongodb server
    Parameters:
        -N/A
    Returns:
        -N/A
    '''
    global client, db, tweets_collection
    client.close()


# i) Search for tweet -------------------------------------------------------------------------------------------------------------
def keyword_tweets(keywords: list) -> list:
    '''
    Retrieves all tweets that match the keyword/s
    Parameters:
        -keywords: ['hello', 'what',....]
    Returns:
        -results: list of json type objects
    '''
    global client, db, tweets_collection
    # appends words to be queried
    key_query = []
    
    for i in keywords:
        # Makes it so that the word is not a substring of another word, but punctuations can be present
        a_holder = { 'content': { '$regex': '(^|\W)' + str(i) + '($|\W)', '$options': 'i' } } #'$options' : 'i' makes it case insensitive
        key_query.append(a_holder)
    query = {
    '$and': key_query
    }
    results = tweets_collection.find(query) # Query the collection
    return list(results)


# ii) Search for users -------------------------------------------------------------------------------------------------------------
def keyword_users(keyword: str) -> list:
    '''
    Retrieves all users whose displayname or location contains the keyword
    Parameters:
        -keyword: 'Akib'
    Returns:
        -results: list of json type objects
    '''
    global client, db, tweets_collection
    #'$options' : 'i' makes it case insensitive
    query = {       
    '$or': [
        { 'user.location': { '$regex': '(^|\W)' + keyword + '($|\W)', '$options': 'i'}},
        { 'user.displayname': { '$regex': '(^|\W)' + keyword + '($|\W)', '$options': 'i'}}
    ]
    
    }
    results = tweets_collection.find(query) # Query the collection
    return list(results)


# iii) List top tweet -------------------------------------------------------------------------------------------------------------
def top_tweets (num: int, field: str) -> list:
    '''
    Retrieves top tweets based on the number and field specified by the user
    Parameters:
        -num: 5
        -field: 'retweetCount'
    Returns:
        -results: list of json type objects
    '''
    global client, db, tweets_collection
    results = tweets_collection.find().sort({ field: -1 }).limit(num) # Query the collection
    return list(results)


# iv) List top users -------------------------------------------------------------------------------------------------------------
def top_users (num: int) -> list:
    '''
    Retrieves top tweets based on the number and field specified by the user
    Parameters:
        -num: 5
    Returns:
        -results: list of json type objects
    '''
    global client, db, tweets_collection
    pipeline = [
        {"$group": {"_id": "$user.id", "user": {"$first": "$user"}, "followersCount": {"$max": "$user.followersCount"}}},
        {"$sort": {"followersCount": -1}},
        {"$limit": num}
    ]

    # Execute the aggregation pipeline
    results = tweets_collection.aggregate(pipeline)    
    return list(results)


# v) Compose a tweet -------------------------------------------------------------------------------------------------------------
def insert_tweet (text: str) -> None:
    '''
    Inserts a new tweet to the database
    Parameters:
        -text: 'Hello how are you'
    Returns:
        -N/A
    '''
    global client, db, tweets_collection
    new_tweet = {
    "url": None,
    "date": datetime.utcnow().isoformat(),
    "content": text,
    "renderedContent": None,
    "id": None,
    "user": {
        "username": "291user",
        "displayname": None,
        "id": None,
        "description": None,
        "rawDescription": None,
        "descriptionUrls": None,
        "verified": None,
        "created": None,
        "followersCount": None,
        "friendsCount": None,
        "statusesCount": None,
        "favouritesCount": None,
        "listedCount": None,
        "mediaCount": None,
        "location": None,
        "protected": None,
        "linkUrl": None,
        "linkTcourl": None,
        "profileImageUrl": None,
        "profileBannerUrl": None,
        "url": None
    },
    "outlinks": None,
    "tcooutlinks": None,
    "replyCount": None,
    "retweetCount": None,
    "likeCount": None,
    "quoteCount": None,
    "conversationId": None,
    "lang": None,
    "source": None,
    "sourceUrl": None,
    "sourceLabel": None,
    "media": None,
    "retweetedTweet": None,
    "quotedTweet": None,
    "mentionedUsers": None
    }

    # Insert the new tweet into the collection
    tweets_collection.insert_one(new_tweet)