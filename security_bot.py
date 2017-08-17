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
                     user_agent =  "Linux:reply_comment_app:v0.1")
sub = reddit.subreddit('netsec+AskNetSec+netsecstudents \
                       +ReverseEngineering+HowToHack+hacking \
                       +security+Malware+networking+crypto')

#-----------------Initialise Lists and Variables-------------------
titles = []
sub_r = []
score = []
comments = []
times = ["week", "year", "all", "day", "hour", "month"]
choice = ''
URL = "http://www.reddit.com"
inp = input("Enter search term or leave blank for full list! ").lower()

#---Function to populate lists of the top submissions' attributes---
def time_filter(time):
    for submission in sub.top('{t}'.format(t=time)):
        if inp in submission.title.lower().split() or inp == "":
            titles.append('<a href="{u}" target="_blank">{name}</a>' \
                  .format(u=URL+submission.permalink, name=submission.title))
            sub_r.append(submission.subreddit_name_prefixed)
            score.append(int(submission.score))
            comments.append(int(submission.num_comments))
        else:
            continue

#--------------Enforce valid user input of time interval-----------
while True:
    time_interval = input("Please enter the time interval: ")#
    if time_interval in times:
        break
    else:
        print("Enter week, year, all, day, hour or month")

time_filter(time_interval)

#------------------------Create Pandas Table-----------------------
table = pd.DataFrame({
    "Titles": titles,
    "Sub-Reddits": sub_r, 
    "Score": score, 
    "Comments": comments 
    })

#-------------Use User Input to choose the Sort method-------------
while choice != "1" or "2":
    print("[1]  To sort by score enter 1")
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

#--Configure Pandas Display Options, Sort Method and Output Format--
def table_output(table):
    pd.set_option('display.max_colwidth', 250)
    pd.set_option('max_rows', 100)
    pd.set_option('colheader_justify', 'left')
    table.sort_values(choice, inplace=True, ascending=False)
    table.to_html('info_sec_table.html', escape=False)

table_output(table)