import backend
from datetime import datetime
import sys
MAX_NUMBER = sys.maxsize


# Unicode
Happy = "\U0001F604"
Sad = "\U0001F614"
CYAN = "\033[96m"
INDIGO = "\033[95m"
RED = "\033[91m"
BOLD = "\033[1m"
UNDER_LINE = "\033[4m"
CLOSE = "\033[0m"

def json_user(json_data) -> dict:
    '''
    Returns user info in json format dict

    Parameters:
        -json_data: json type object
    Returns:
        -user: a dictionary containing the user fields

    '''
    return json_data['user']

def info_tweet(json_data) -> str:
    '''
    Returns tweet info
    Parameters:
        -json_data: json type object
    Returns:
        -tweet_id: '655f1469787220b6f884a1f8'
        -tweet_date: '2021-03-30T03:33:23+00:00'
        -tweet_content: 'bla bla bla'
        -username: 'kaursuk06272818'
    '''
    tweet_id = json_data['_id']
    tweet_date = json_data['date']
    tweet_content = json_data['content']
    username = json_data['user']['username']

    return tweet_id, tweet_date, tweet_content, username


def info_userLocation(json_data) -> str:
    '''
    Returns user info (Location is included but Follower count isn't)
    Parameters:
        -json_data: json type object
    Returns:
        -user_id: '655f1469787220b6f884a1f8'
        -username: 'kaursuk06272818'
        -display_name: 'KAUR SUKH'
        -location: 'Azm Uttar Pradesh, India'
    '''
    user_id = json_data['user']['id']
    username = json_data['user']['username']
    display_name = json_data['user']['displayname']
    location = json_data['user']['location']

    return user_id, username, display_name, location


def info_userfollowersCount(json_data) -> str:
    '''
    Returns user info (Follower count is included but Location isn't)
    Parameters:
        -json_data: json type object
    Returns:
        -user_id: '655f1469787220b6f884a1f8'
        -username: 'kaursuk06272818'
        -display_name: 'KAUR SUKH'
        -follower_count: '10'
    '''
    user_id = json_data['user']['id']
    username = json_data['user']['username']
    display_name = json_data['user']['displayname']
    follower_count = json_data['user']['followersCount']

    return user_id, username, display_name, follower_count


def dicToList(input_dict) -> list:
    """
    Returns a list of strings from a dictionary
    Parameters:
        - input_dict: dictionary to be converted
    Returns:
        - result_list: list of strings
    """
    result_list = []
    for key, value in input_dict.items():
        result_list.append(f"{key}: {value}\n")
    return result_list


def printField(strings, max_line_length = 90) -> None:
    """
    Returns a list of strings in a bigger box format
    Parameters:
        - strings: list of strings to be printed
        - max_line_length: max length of each line
    Returns:
        - None
    """
    print("\n")
    print("+" + "-" * (max_line_length + 2) + "+")
    for line in strings:
        words = line.split()
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 <= max_line_length:
                current_line += word + " "
            else:
                print("| " + current_line.ljust(max_line_length) + " ")
                current_line = word + " "
        print("| " + current_line.ljust(max_line_length) + " ")
        print("|")
    print("+" + "-" * (max_line_length + 2) + "+")


def printBox(strings, max_line_length = 50) -> None:
    """
    Returns a list of strings in a box format
    Parameters:
        - strings: list of strings to be printed
        - max_line_length: max length of each line
    Returns:
        - None
    """
    print("\n")
    print("+" + "-" * (max_line_length + 2) + "+")
    for line in strings:
        words = line.split()
        current_line = ""
        for word in words:
            if len(current_line) + len(word) + 1 <= max_line_length:
                current_line += word + " "
            else:
                print("| " + current_line.ljust(max_line_length) + " ")
                current_line = word + " "
        print("| " + current_line.ljust(max_line_length) + " ")
    print("+" + "-" * (max_line_length + 2) + "+")


def validateInput(input, min, max) -> bool:
    '''
    Parameters:
        - input: input to be validated
        - min: 1, 2, 3, ...
        - max: 1, 2, 3, ...
        eg: validateInput(input, 1, 1, 6)
    Returns:
        - True if input is valid
        - False if input is invalid
    '''
    if input.isdigit() == True:
        input = int(input)
        if input < min:
            text = [f"{RED}Invalid input{CLOSE}",
                    f"Input has to be equal to or above {min}. Returning to Main menu..."]
            printBox(text)
            return False
        elif input > max:
            text = [f"{RED}Invalid input{CLOSE}",
                    f"Input has to be equal to or below {max}. Returning to Main menu..."]
            printBox(text)
            return False
    else:
        text = [f"{RED}Invalid input{CLOSE}",
                "Input has to be a number. Returning to Main menu..."]
        printBox(text)
        return False
    return True


def displayMenu() -> str:
    '''
    Displays User menu listing
    - Search for tweets
    - Search for users
    - List top tweets
    - List top users
    - Compose a tweet
    Parameters:
        None
    Returns:
        str: User's choice from the menu
    '''
    text = [f"{BOLD}{UNDER_LINE}{CYAN}Welcome to Twitter!{CLOSE}",
            "\n",
            f"{BOLD}Please choose one of the following options{CLOSE}",
            f"{RED}1{CLOSE} Search for tweets",
            f"{RED}2{CLOSE} Search for users",
            f"{RED}3{CLOSE} List top tweets",
            f"{RED}4{CLOSE} List top users",
            f"{RED}5{CLOSE} Compose a tweet",
            f"{RED}6{CLOSE} Exit"]
    printBox(text)

    user_choice = input(f"{BOLD}Enter the number of your choice: {CLOSE}")

    return user_choice


def searchTweet() -> None:
    '''
    The user should be able to provide one or more keywords, and the system should retrieve all 
    tweets that match all those keywords (AND semantics). A keyword matches if it appears in the content field. 
    For each matching tweet, display the id, date, content, and username of the person who posted it. 
    The user should be able to select a tweet and see all fields.
    Parameters:
        None
    Returns:
        - None          
    '''
    text = [f"{CYAN}{UNDER_LINE}Search for tweets{CLOSE}",
            "\n",
            f"{BOLD}Please enter one or more keywords separated by spaces or punctuations.{CLOSE}"]
    printBox(text)

    keywords = input(f"{BOLD}Enter keywords: {CLOSE}")

    if keywords.strip():
        keywords_list = keywords.split(" ")
    else:
        text = [f"{RED}Invalid input{CLOSE}",
                "Input cannot be empty or just space. Returning to Main menu..."]
        printBox(text)
        return    

    list_of_tweets = backend.keyword_tweets(keywords_list)
    tweet_number = 0

    for tweet in list_of_tweets:
        tweet_number += 1

        tweet_id, tweet_date, tweet_content, username = info_tweet(tweet)

        # Convert date to readable format
        parsed_date = datetime.fromisoformat(tweet_date.replace("Z", "+00:00"))
        formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S")

        text = [f"{RED}# {tweet_number}{CLOSE}",
                f"{INDIGO}Tweet ID:{CLOSE}      {tweet_id}",
                f"{INDIGO}Tweet Date:{CLOSE}    {formatted_date}",
                f"{INDIGO}User name:{CLOSE}      {username}",
                "\n",
                f"{INDIGO}Tweet Content{CLOSE}",
                f"{tweet_content}"]
        printBox(text)

    if list_of_tweets == []:
        text = [f"No tweets found {Sad}"]
        printBox(text)
        return
    
    else:
        text = [f"{BOLD}Please enter the {RED}tweet number{CLOSE} {BOLD}you want to view{CLOSE}",
                "OR",
                f"{BOLD}Enter {RED}M{CLOSE} {BOLD}to return to Main menu{CLOSE}"]
        printBox(text)

        user_choice = input(f"{BOLD}Enter your choice: {CLOSE}")

        if user_choice.upper() == "M":
            return
        
        else:

            if validateInput(user_choice, 1, tweet_number) == False:
                return
            
            else:
                tweet_number = int(user_choice)
                tweet = list_of_tweets[tweet_number - 1]
                text = dicToList(tweet)
                printField(text)
                user_choice = input(f"{BOLD}Enter any key to return to Main menu: {CLOSE}")
                return


def searchUser() -> None:
    '''
    The user should be able to provide a keyword  and see all users whose displayname or location contain the keyword. 
    For each user, list the username, displayname, and location with no duplicates. The user should be able to 
    select a user and see full information about the user.
    Parameters:
        - input1. and how the input looks like
        - input2. and how the input looks like
    Returns:
        - return. and how the return value looks like
    '''
    text = [f"{CYAN}{UNDER_LINE}Search for users{CLOSE}",
            "\n",
            f"{BOLD}Please enter a keyword: {CLOSE}"]
    printBox(text)

    keywords = input(f"{BOLD}Enter keywords: {CLOSE}")
    if keywords.strip():
        list_of_users = backend.keyword_users(keywords)
    else:
        text = [f"{RED}Invalid input{CLOSE}",
                "Input cannot be empty or just space. Returning to Main menu..."]
        printBox(text)
        return
    user_number = 0

    # Using sets to remove duplicates
    processed_usernames = set()
    display_users = []

    for user in list_of_users:

        user_id, username, display_name, location = info_userLocation(user)
        if user_id not in processed_usernames:
            user_number += 1
            text = [f"{RED}# {user_number}{CLOSE}",
                    f"{INDIGO}User name:{CLOSE}      {username}",
                    f"{INDIGO}Display name:{CLOSE}  {display_name}",
                    f"{INDIGO}Location:{CLOSE}      {location}"]
            printBox(text)
            processed_usernames.add(user_id)
            display_users.append(user)


    if list_of_users == []:
        text = [f"No users found {Sad}"]
        printBox(text)
        return
    
    else:
        text = [f"{BOLD}Please enter the {RED}user number{CLOSE} {BOLD}you want to view{CLOSE}",
                f"{BOLD}Enter {RED}M{CLOSE} {BOLD}to return to Main menu{CLOSE}"]
        printBox(text)

        user_choice = input(f"{BOLD}Enter your choice: {CLOSE}")

        if user_choice.upper() == "M":
            return
        
        else:
            if validateInput(user_choice, 1, user_number) == False:
                return
            else:
                user_number = int(user_choice)
                user = display_users[user_number - 1]
                user = json_user(user)
                text = dicToList(user)
                printField(text)
                user_choice = input(f"{BOLD}Enter any key to return to Main menu: {CLOSE}")
                return


def listTopTweet(tweet_count, field) -> None:
    '''
    The user should be able to list top n tweets based on any of the fields retweetCount, likeCount, quoteCount, 
    to be selected by the user. The value of n will be also entered by the user. The result will be ordered in 
    a descending order of the selected field. For each matching tweet, display the id, date, content, and username of 
    the person who posted it. The user should be able to select a tweet and see all fields.
    Parameters:
        - input1 number of tweets to be displayed
        - input2 field to be sorted by
    Returns:
    '''
    if field == "1":
        field = "retweetCount"
    elif field == "2":
        field = "likeCount"
    elif field == "3":
        field = "quoteCount"
    else:
        print("Invalid input")
        return
    
    list_of_tweets = backend.top_tweets(int(tweet_count), field)
    tweet_number = 0

    for tweet in list_of_tweets:
        tweet_number += 1
        tweet_id, tweet_date, tweet_content, username = info_tweet(tweet)

        # Convert date to readable format
        parsed_date = datetime.fromisoformat(tweet_date.replace("Z", "+00:00"))
        formatted_date = parsed_date.strftime("%Y-%m-%d %H:%M:%S")

        text = [f"{RED}# {tweet_number}{CLOSE}",
                f"{INDIGO}Tweet ID:{CLOSE}      {tweet_id}",
                f"{INDIGO}Tweet Date:{CLOSE}    {formatted_date}",
                f"{INDIGO}User name:{CLOSE}      {username}",
                "\n",
                f"{INDIGO}Tweet Content{CLOSE}",
                f"{tweet_content}"]
        printBox(text)

    if list_of_tweets == []:
        text = [f"No tweets found {Sad}"]
        printBox(text)
        return
    
    else:
        text = [f"{BOLD}Please enter the {RED}tweet number{CLOSE} {BOLD}you want to view{CLOSE}",
                f"{BOLD}Enter {RED}M{CLOSE} {BOLD}to return to Main menu{CLOSE}"]
        printBox(text)
        user_choice = input(f"{BOLD}Enter your choice: {CLOSE}")

        if user_choice.upper() == "M":
            return
        
        else:
            if validateInput(user_choice, 1, tweet_number) == False:
                return
            
            else:
                tweet_number = int(user_choice)
                tweet = list_of_tweets[tweet_number - 1]
                text = dicToList(tweet)
                printField(text)
                user_choice = input(f"{BOLD}Enter any key to return to Main menu: {CLOSE}")
                return


def listTopUser(user_count) -> None:
    '''
    The user should be able to list top n users based on followersCount with n entered by user. For each user, list the 
    username, displayname, and followersCount with no duplicates. The user should be able to select a user and see the full 
    information about the user.
    Parameters:
        - input number of users to be displayed
    Returns:
        - None
    '''
    list_of_users = backend.top_users(int(user_count))
    user_number = 0

    # Using sets to remove duplicates
    processed_usernames = set()
    display_users = []

    for user in list_of_users:
        
        user_id, username, display_name, follower_count = info_userfollowersCount(user)

        if user_id not in processed_usernames:
            user_number += 1
            text = [f"{RED}# {user_number}{CLOSE}",
                    f"{INDIGO}User name:{CLOSE}          {username}",
                    f"{INDIGO}Display name:{CLOSE}      {display_name}",
                    f"{INDIGO}Follower count:{CLOSE}    {follower_count}"]
            printBox(text)
            processed_usernames.add(user_id)
            display_users.append(user)

    if list_of_users == []:
        text = [f"No users found {Sad}"]
        printBox(text)
        return
    
    else:
        text = [f"{BOLD}Please enter the {RED}user number{CLOSE} {BOLD}you want to view{CLOSE}",
                f"{BOLD}Enter {RED}M{CLOSE} {BOLD}to return to Main menu{CLOSE}"]
        printBox(text)
        user_choice = input(f"{BOLD}Enter your choice: {CLOSE}")

        if user_choice.upper() == "M":
            return
        
        else:
            if validateInput(user_choice, 1, user_number) == False:
                return
            
            else:
                user_number = int(user_choice)
                user = display_users[user_number - 1]
                user = json_user(user)
                text = dicToList(user)
                printField(text)
                user_choice = input(f"{BOLD}Enter any key to return to Main menu: {CLOSE}")
                return
            

def composeTweet() -> None:
    '''
    The user should be able to compose a tweet by entering a tweet content. Your system should insert the tweet to 
    the database, set the date filed to the system date and username to "291user". All other fields will be null.
    Parameters:
        None
    Returns:
        - return. and how the return value looks like
    '''
    text = [f"{CYAN}{UNDER_LINE}Compose a tweet{CLOSE}",
            "\n",
            f"{BOLD}Please enter the tweet content{CLOSE}"]
    printBox(text)

    tweet_content = input(f"{BOLD}Enter tweet content:{CLOSE}")

    if tweet_content.strip():
        backend.insert_tweet(tweet_content)
    else:
        text = [f"{RED}Invalid input{CLOSE}",
                "Content cannot be empty or just space. Returning to Main menu..."]
        printBox(text)
        return

    text = [f"Tweet successfully Posted! {Happy}",
            f"Returning to Main menu..."]
    printBox(text)

    return



def exitProgram() -> bool:
    '''
    Option to end the program
    '''
    text = [f"Are you sure you want to {BOLD}Exit{CLOSE}?",
            f"{RED}Y{CLOSE} / {RED}N{CLOSE}"]
    printBox(text)

    user_choice = input(f"{BOLD}Enter your choice: {CLOSE}")
    
    if user_choice.upper() == "Y":
        text = [f"Thank you for using Twitter! {Happy}"]
        printBox(text)
        backend.connect_close()
        sys.exit()

    elif user_choice.upper() == "N":
        text = ["Returning to Main menu..."]
        printBox(text)
        return False
        
    else:
        text = [f"{RED}Invalid input{CLOSE}",
                "Returning to Main menu..."]
        printBox(text)
        return False


def main():
    '''
    Main function
    '''
    # While loop to connect to backend
    while True:
        text = [f"{BOLD}Please enter the {RED}port number{CLOSE} {BOLD}of the database server.{CLOSE}"]
        printBox(text)

        port_number = input(f"{BOLD}Enter port number: {CLOSE}")
        
        try :
            #port_number = 61448
            connected = backend.connect_dbserver(port_number)
            break
        except:
            text = [f"{RED}Invalid input{CLOSE}",
                    "Input has to be a number. Please try again..."]
            printBox(text)
            

    # While loop to display menu
    while True:
        user_choice = displayMenu()

        if validateInput(user_choice, 1, 6) == False:
            continue

        if user_choice == "1":
            searchTweet()

        elif user_choice == "2":
            searchUser()

        elif user_choice == "3":
            text = [f"{CYAN}{UNDER_LINE}List of top tweets{CLOSE}",
                    "\n",
                    f"{BOLD}Please enter the number of tweets to be displayed{CLOSE}"]
            printBox(text)

            tweet_count = input(f"{BOLD}Enter the number of tweets: {CLOSE}")

            # Input validation
            if validateInput(tweet_count, 1, MAX_NUMBER) == False:
                continue

            text = [f"{BOLD}Please enter the field to be sorted by{CLOSE}",
                    f"{RED}1{CLOSE} Retweet Count",
                    f"{RED}2{CLOSE} Like Count",
                    f"{RED}3{CLOSE} Quote Count"]
            printBox(text)

            field = input(f"{BOLD}Enter field: {CLOSE}")

            # Input validation
            if validateInput(field, 1, 3) == False:
                continue
            listTopTweet(tweet_count, field)

        elif user_choice == "4":

            text = [f"{CYAN}{UNDER_LINE}List top users{CLOSE}",
                    "\n",
                    f"{BOLD}Please enter the number of users to be displayed: {CLOSE}"]
            printBox(text)

            user_count = input(f"{BOLD}Enter number of users: {CLOSE}")

            # Input validation
            if validateInput(user_count, 1, MAX_NUMBER) == False:
                continue

            listTopUser(user_count)

        elif user_choice == "5":
            composeTweet()

        elif user_choice == "6":
            answer = exitProgram()

            if answer == True:
                break
            else:
                continue
            
    return
if __name__ == "__main__":
    main()
