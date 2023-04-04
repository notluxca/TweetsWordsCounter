import os
import time
from pandas import DataFrame
from collections import Counter
from snscrape.modules.twitter import TwitterSearchScraper


def mainAppMenu():
    os.system("cls")
    print("""
   _____                 _         _____                   _            
  |_   _|               | |       /  __ \                 | |           
    | |_      _____  ___| |_ ___  | /  \/ ___  _   _ _ __ | |_ ___ _ __ 
    | \ \ /\ / / _ \/ _ \ __/ __| | |    / _ \| | | | '_ \| __/ _ \ '__|
    | |\ V  V /  __/  __/ |_\__ \ | \__/\ (_) | |_| | | | | ||  __/ |   
    \_/ \_/\_/ \___|\___|\__|___/  \____/\___/ \__,_|_| |_|\__\___|_|   """)
    print("\n             by Lindo Lucas, bjs a todos\n\n")

    username = input("Provide a twitter username: ")
    query = f"(from:{username})"
    # get parameters to make the search
    try:
        limit = int(input("How much tweets do you want to count words (enter a number): "))
    except ValueError:
        print(f"This is not a number")
        time.sleep(2)
        mainAppMenu()
    try:
        wordsRank = int(input("How much words do you want to rank (enter a number): "))
    except ValueError:
        print(f"This is not a number")
        time.sleep(2)
        mainAppMenu()

    print("\nCounting words, please wait...")
    print("The time to complete this may vary depending on your computer\nand on your internet speed, so please, be fucking patient")
    tweets = []

    for tweet in TwitterSearchScraper(query).get_items():
        if len(tweets) == limit:
            break
        else:
            tweets.append([tweet.rawContent])

    df = DataFrame(tweets, columns=['Tweet'])
    df.to_csv('tweets.txt') # dont ask me why
    splited_words_data = df.to_string().split()
    counter = Counter(splited_words_data)   
    most_occur = counter.most_common(wordsRank)
    # ^^ this saves the words data from every single tweet, saves into a txt file formated

    filename = f"{username}_TweetsCount.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for item in most_occur:
            f.write(f"{item[0]}: {item[1]}\n")
    print(f"\nResults saved to {filename}. (file should be on the same directory\nwhere the program was first runned)")
    print("Type 'open' to view data or press enter to start again")
    choice = input("> ")
    if choice.lower() == 'open':
        os.system(f"notepad.exe {username}_TweetsCount.txt")
    else:
        mainAppMenu()


run = True

while run:
    mainAppMenu()
    


"""
                                            _.oo.
                 _.u[[/;:,.         .odMMMMMM'
              .o888UU[[[/;:-.  .o@P^    MMM^
             oN88888UU[[[/;::-.        dP^
            dNMMNN888UU[[[/;:--.   .o@P^
           ,MMMMMMN888UU[[/;::-. o@^
           NNMMMNN888UU[[[/~.o@P^
           888888888UU[[[/o@^-..
          oI8888UU[[[/o@P^:--..
       .@^  YUU[[[/o@^;::---..
     oMP     ^/o@P^;:::---..
  .dMMM    .o@^ ^;::---...
 dMMMMMMM@^`       `^^^^
YMMMUP^   
 ^^
 
"""