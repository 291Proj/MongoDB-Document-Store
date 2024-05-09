




def info_tweet(json_data) ->str:
    '''
    Returns tweet info

    Parameters:
        -json_data: json type object
    Returns:
        -tweet_id: '655f1469787220b6f884a1f8'
        -tweet_date: '2021-03-30T03:33:23+00:00'
        -tweet_content: 'blab bla bla'
        -username: 'kaursuk06272818'
    '''
 

    tweet_id = json_data['_id']
    tweet_date = json_data['date']
    tweet_content = json_data['content']
    username = json_data['user']['username']

    return tweet_id, tweet_date, tweet_content, username
    



def info_userLocation(json_data) ->str:
    '''
    Returns user info (Location is included but Follower count isn't)

    Parameters:
        -json_data: json type object
    Returns:
        -username: 'kaursuk06272818'
        -display_name: 'KAUR SUKH'
        -location: 'Azm Uttar Pradesh, India'
    '''
 
 
    location = json_data['user']['location']
    display_name = json_data['user']['displayname']
    username = json_data['user']['username']

    return username, display_name, location


def json_user(json_data) -> dict:
    '''
    Returns user info in json format dict

    Parameters:
        -json_data: json type object
    Returns:
        -user: a dictionary containing the user fields

    '''

    return json_data['user']



def info_userfollowersCount(json_data) ->str:
    '''
    Returns user info (Follower count is included but Location isn't)

    Parameters:
        -json_data: json type object
    Returns:
        -username: 'kaursuk06272818'
        -display_name: 'KAUR SUKH'
        -follower_count: '10'
    '''
 
 
    follower_count = json_data['user']['followersCount']
    display_name = json_data['user']['displayname']
    username = json_data['user']['username']

    return username, display_name, follower_count