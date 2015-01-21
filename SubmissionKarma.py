import operator
import praw

# Enter account details here
username = ''
password = ''
# Enter the name of the user to get
# submission karma for
user = ''

r = praw.Reddit(user_agent='u\Testing 1.0')
r.login(username, password)
user_name = user
user = r.get_redditor(user_name)
thing_limit = None
gen = user.get_submitted(limit=thing_limit)
karma_by_subreddit = {}
for thing in gen:
    subreddit = thing.subreddit.display_name
    karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + thing.score)
#toPrint = karma_by_subreddit.items()
toPrint = sorted(karma_by_subreddit.items(), key=operator.itemgetter(1), reverse=True)

karma = 0
for item in karma_by_subreddit.values():
    karma = karma + item
f = open('SubmissionKarma.txt','w')
f.write(str(toPrint)) # python will convert \n to os.linesep
f.write("\nTotal: " + str(karma))
f.close() 
#print (str(toPrint))
