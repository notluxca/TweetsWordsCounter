# TweetsWordsCounter ( NOT WORKING ANYMORE )
----------
- Update log (21/08/2023)
twitter has changed its api, so you cannot access or search tweets if you dont have an account logged in, so
this app will be no longer working until they change it
it was good while it lasted
---------
This is a python script that count how much words someone said in a certain quantity of tweets
- uses snscrape and pandas

![alt text](https://media.discordapp.net/attachments/935739172164083743/1092956544435486810/image.png)

- Provide an username (@) to search
- provide a certain number of tweets you want to count words
- provide how much words you want in the rank list

![alt text](https://media.discordapp.net/attachments/935739172164083743/1092963360577945690/image.png)

- wait until the process is finished, this may take a while depending on your parameters, processing power, or internet speed, but 
should not take tooo long, on my computer, I had a 7 minutes wait time to process 20k tweets

after this is done the program will save the results to a txt file located on the same directory the script was executed,
you will have the choice to automatically open the txt file containg the results.

![alt text](https://media.discordapp.net/attachments/935739172164083743/1092964972084068392/image.png)


# How to use
- install Python3+ 
- Install pandas with "pip install pandas"
- Install snscrape with "pip install snscrape"
- run the script
