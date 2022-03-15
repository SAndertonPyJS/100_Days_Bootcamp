### --- PROVIDED CODE --- ###

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    total_likes = total_likes + post['Likes']


print(total_likes)

### --- SOLUTION --- ###

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    #in this example we use try except to go through each post and it want to find the total likes
    #for all posts. If we can't find a like instead of throwing a key error we use try/except to 
    #instead add 0 likes to the count. Same effect and we don't have to edit the dict for every entry.
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes +=0


print(total_likes)
