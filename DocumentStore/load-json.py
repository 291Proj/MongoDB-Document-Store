import json
import pymongo
import sys

def load_json_to_mongo(json_file, mongo_port):
    # Connect to MongoDB
    client = pymongo.MongoClient(f'mongodb://localhost:{mongo_port}/')

    # Create or get the database
    db = client['291db']

    # Drop existing 'tweets' collection if it exists
    if 'tweets' in db.list_collection_names():
        db['tweets'].drop()

    # Create 'tweets' collection
    tweets_collection = db['tweets']

    # Batch size for insertMany
    batch_size = 10000
    batch = []

    # Read JSON file line by line and insert in batches
    with open(json_file, 'r') as file:
        for line in file:
            tweet = json.loads(line)
            batch.append(tweet)

            if len(batch) == batch_size:
                tweets_collection.insert_many(batch)
                batch = []

    # Insert any remaining tweets in the last batch
    if batch:
        tweets_collection.insert_many(batch)


if __name__ == "__main__":
    if len(sys.argv) != 3: #need to 3 arguments from command line
        sys.exit(1)

    json_file = sys.argv[1] 
    mongo_port = int(sys.argv[2])

    load_json_to_mongo(json_file, mongo_port)



# python load-json.py 100.json 27017