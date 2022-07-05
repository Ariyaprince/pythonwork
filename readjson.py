# json -javascript object notation
# transfer data

import json
with open("blogs.json",encoding="utf-8")as f:
    data=json.load(f)
    print(data)
print(len(data))

# no fo post by userid 1
post_usre1=[post for post in data if post["userId"]==1]
print(len(post_usre1))

# total no of likes for postid 6

postid_6=[post["liked_by"] for post in data if post["postId"]==6]
print(len(postid_6[0]))

# no of post liked by user=2
num_by_user2=[post for post in data if 2 in post["liked_by"]]
print(len(num_by_user2))