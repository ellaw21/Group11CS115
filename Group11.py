#Ella Warnock, Lewis Goldenberg, Keyaan Gala
#I pledge my honor that I have abided by the Stevens Honor System.



#Dictionary that contains userID as key and stores the list of user preferences
users = {}

def preferences(userID):
    if userID not in users.keys():
        users[userID] = []
        
    """Takes in an artist that user likes. Stores all artists in global list artistsList
    Author:Ella"""
    i = 1
    while i == 1 :
        artist = input("Enter an artist that you like (Enter to finish):")
        if artist == "":
            i = 0
        else:
            users[userID].append(artist)

def welcome():
    """Takes no inputs. Gives greeting and prompts user to enter their name
    Author:Ella"""
    userID = input("Enter your name (put a $ symbol after your name if you wish your preferences to remain private):")
    if userID not in users:
        preferences(userID)
    return userID


#current user name
name = welcome()



def numMatches(u1, u2):
    """returns the number of matches of two artists in lists
    Author: Ella"""
    count = 0
    for i in u1:
        if i in u2:
            count += 1
    return count
            
def bestUserMatch(prefs, allPrefs):
    """Given a list of preferences and a list of lists of preferences,
    returns the one with the most matches
    Author:Ella"""
    if prefs == [] or allPrefs == []:
        print("No recommendations available at this time.")
        return
    maxMatches = 0
    bestIndex = 0
    for i in range(len(allPrefs)):
        currentMatches = numMatches(prefs, allPrefs[i])
        if currentMatches > maxMatches:
            bestIndex = i
            maxMatches = currentMatches
    if maxMatches == 0:
        print("No recommendations available at this time.")
        return
    else:
        count = 0
        for i in allPrefs[bestIndex]:
            if i not in prefs:
                count+=1
                print(i)
        if count == 0:
            print("No recommendations available at this time.")

def recommendations(userID):
    """Returns user recommendations
    Author:Ella"""
    allPreferences = []
    for i in users:
        if i[len(i)-1] != "$":
            allPreferences.append(users[i])
    bestUserMatch(users[userID], allPreferences)

def popularArtists():
    """Does not take an input. Returns the most popular artists
    Author:Keeyan"""
    allArtists = []
    for user_prefs in users.values():
        allArtists.extend(user_prefs)

    if not allArtists:
        print("No preferences available. Add preferences first.")
        return

    artist_counts = {}
    for artist in allArtists:
        artist_counts[artist] = artist_counts.get(artist, 0) + 1

    most_popular_artist = max(artist_counts, key=artist_counts.get)


def howPopular(name, preferences):
    """Does not take an input. Returns how popular the most
    popular artist is using how many recommendations it has been given
    Author:Lewis"""
    singers = []
    seen = {}
    for users in preferences:
        singers = singers + preferences[users]
    for item in singers:
        if item in seen:
            seen[item]+=1
        else: seen[item] = 1
    for item in singers:
        out = 0
        if seen[item] > out:
            out = seen[item]
    print(out)
    menu(name,preferences)


def mostLikes():
    """Does not take an input. Returns the user with the most
    amount of liked artists
    Author:Keyaan"""
    if not users:
        print("No users available. Add preferences first.")
        return
    max_likes_user = max(users, key=lambda user: len(users[user]))
    print(f"The user with the most likes is: {max_likes_user}")

    #Iterate through users dictionary and find the list with the most amount of artists and returns it


def menu(name, preferences):
    """Displays options for the user.Once user inputs desired option
    it runs the function associated with the input.
    Once that function is completed, runs in a while loop till save
    and quit option is input
    Author:Lewis"""
    user_input=input("Enter a letter to choose an option:\n e - Enter preferences\n r - Get recommendations\n p - Show most popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n q - Save and quit\n")
    while True:
        if user_input == 'e':
            preferences(name)
        if user_input == 'r':
            recommendations(name)
        if user_input == 'p':
            popularArtist()
        if user_input == 'h':
            howPopular()
        if user_input == 'm':
            mostLikes()
        if user_input == 'q':
            save_quit(name, preferences)
            break
        if user_input not in['e', 'r', 'p', 'h', 'm', 'q']:
            user_input=input("Enter a letter to choose an option:\n e - Enter preferences\n r - Get recommendations\n p - Show most popular artists\n h - How popular is the most popular\n m - Which user has the most likes\n q - Save and quit\n")


def save_quit(name, preferences):
    """Does not take an input. Saves the users preferences
    Author:Lewis"""
    f=open("musicrecplus.txt","w")
    for item in preferences:
        newstr = str(preferences[item]).replace("[",":")
        newerstr = newstr.replace("]","")
        newererstr = newerstr.replace(", ",",")
        newerererstr = newererstr.replace("'","")
        print(item+newerererstr)
        f.write(item+newerererstr+"\n")
    f.close()
    quit()

#call options to begin running the music code
menu(name,users[name])

