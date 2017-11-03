'''
Python 3.5.2 script which outputs to html upto 100 of the highest scoring 
reddit posts from the top 10 information security subreddits. 
The user can select the time interval of the top submissions
e.g. day, week, all; and the order the submissions are listed 
e.g. by highest score or most commented.
'''
import praw
import pandas as pd

import config

#---------Create read-only Reddit and sub-reddit instances---------
reddit = praw.Reddit(client_id = config.client_id,
                     client_secret = config.client_secret,
                     user_agent =  config.user_agent)
sub = reddit.subreddit('netsec+AskNetSec+netsecstudents \
                       +ReverseEngineering+HowToHack+hacking \
                       +security+Malware+networking+crypto')

#-----------------Initialise Lists and Variables-------------------
titles = []
sub_r = []
score = []
comments = []
times = ["hour", "day", "week", "month", "year", "all"]
choice = ''
URL = "http://www.reddit.com"
inp = input("Enter search term or leave blank for full list! ").lower()

#-----------------------------Populate lists-----------------------
def pop_func(submission):
    titles.append('<a href="{u}" target="_blank">{name}</a>' \
          .format(u=URL+submission.permalink, name=submission.title))
    sub_r.append(submission.subreddit_name_prefixed)
    score.append(int(submission.score))
    comments.append(int(submission.num_comments))

def time_filter(time):
    if inp:
        for submission in sub.search(inp,sort="relevance",syntax="lucene" \
                             ,time_filter="{t}".format(t=time)):
            pop_func(submission)
    else:
        for submission in sub.top('{t}'.format(t=time)):
            pop_func(submission)

#--------------Enforce valid user input of time interval-----------
while True:
    time_interval = input("Please enter the time interval: ")#
    if time_interval in times:
        break
    else:
        print("Enter hour, day, week, month, year or all")

time_filter(time_interval)

#-------------Use User Input to choose the Sort method-------------
while choice != "1" or "2":
    print("\n[1]  To sort by score enter 1")
    print("[2]  To sort by comments enter 2\n")
    choice = input("How would you like the submissions sorted ")
    if choice == "1":
        choice = "Score"
        break
    elif choice == "2":
        choice = "Comments"
        break
    else:
        continue

#--Create and Configure Pandas Display, Sort Method and Output Format--
def table_output():
    table = pd.DataFrame({
        "Titles": titles,
        "Sub-Reddits": sub_r, 
        "Score": score, 
        "Comments": comments 
        })
    
    pd.set_option('display.max_colwidth', 250)
    pd.set_option('max_rows', 100)
    pd.set_option('colheader_justify', 'left')
    table.sort_values(choice, inplace=True, ascending=False)
    table.to_html('info_sec_table.html', escape=False)

table_output()