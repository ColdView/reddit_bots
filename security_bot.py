'''
Experiments using r/netsec
'''
import praw
import config
#---------Create read-only Reddit and sub-reddit instances--------
reddit = praw.Reddit(client_id = config.client_id,
		client_secret = config.client_secret,
		user_agent =  "Linux:reply_comment_app:v0.1")
subreddit = reddit.subreddit('netsec+AskNetSec+netsecstudents+ReverseEngineering+HowToHack+hacking+security+Malware+networking')
#--------------Monitor new Submissions on a SubReddit---------------
string = 'python'
py_posts = [] 
for submission in subreddit.top('week'):
		py_posts.append(submission.title)
print(py_posts)

