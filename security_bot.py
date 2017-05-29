'''
Script which outputs to html the 100 highest scoring reddit posts
of the last week from the top 10 information security subreddits.
'''
import praw
import config
import pprint
import pandas as pd

#---------Create read-only Reddit and sub-reddit instances---------
reddit = praw.Reddit(client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent =  "Linux:reply_comment_app:v0.1")
sub = reddit.subreddit('netsec+AskNetSec+netsecstudents+ReverseEngineering+HowToHack+hacking+security+Malware+networking+crypto')

#-------------------------Initialise lists-------------------------
titles = []
sub_r = []
score = []
comments = []
links = []
URL = "http://www.reddit.com"

#----------Create lists of the top submissions attributes----------
for submission in sub.top('week'):
		titles.append(submission.title)
		sub_r.append(submission.subreddit_name_prefixed)
		score.append(submission.score)
		comments.append(submission.num_comments)
		links.append('<a href="{u}">{name}</a>'.format(u=URL+submission.permalink, name="link"))

#----------------------Create Pandas table-------------------------
table = pd.DataFrame({
        "Titles": titles,
        "Link": links,
        "Sub-Reddits": sub_r, 
        "Score": score, 
        "Comments": comments, 
    })
#-----------------Configure Pandas Table Display Options-----------
pd.set_option('display.max_colwidth', 150)
pd.set_option('max_rows', 100)
pd.set_option('colheader_justify', 'left')
table.to_html('red_sec.html', escape=False)