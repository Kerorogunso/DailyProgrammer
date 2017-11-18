import praw

reddit = praw.Reddit(client_id='aIe9JHEIL2HJYw',
                     client_secret='AtnS3YR1meKQpKweTk16viCsTHk',
                     user_agent='windows:com.example.myredditapp:v0.0.1 (by /u/ChickenChopSuey)'
                     )

top_3 = reddit.subreddit("dailyprogrammer").top(time_filter='week')
for x in top_3:
    print(x.title)


search_string = input("Enter the challenge number: ")
easy_submission = reddit.subreddit("dailyprogrammer").search('Challenge #' + search_string + ' [',sort="date")
for post in easy_submission:
    print(post.title)

