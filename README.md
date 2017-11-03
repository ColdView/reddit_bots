## Reddit Bots

1. #### security_bot.py 
   This bot creates a pandas table of either the top 100 submissions from the top 10 information security sub-reddits or a table of submissions matching the users query. The user can select the date range to capture submissions from such as week, month, all etc. and also the sort method by comments or score. The sorted table is then output to html with hyperlinks.
   For example [this table](https://rawgit.com/ColdView/reddit_bots/master/info_sec_table.html) was output when the user entered buffer as a search term, year as the interval and score as sort method. 
