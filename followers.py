import json
import random

try:
    with open("followers.json",encoding="utf-8") as f:
        data=json.load(f)
        print(data)

    all_users=[user["id"] for user in data]
    print(all_users)
    my_followings=[user["followers"] for user in data if user["username"]=="akhil"][0]
    print(my_followings)
    my_id=[user["id"] for user in data if user["username"]=="akhil"].pop()
    print(my_id)
    to_follow=set(all_users)-set(my_followings)
    to_follow.remove(my_id)
    print(to_follow)

    suggestions=random.sample([*to_follow],2)
    print(suggestions)

except Exception as e:
    print(e.__class__)
