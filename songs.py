# total songs in album 1
import random
from functools import reduce
import json
with open("songs.json",encoding="utf-8") as f:
    data=json.load(f)
# album1_song=[song for song in data if song["album"]=="album1"]
# # print(len(album1_song))

# album_song=list(filter(lambda song:song["album"]=="album1",data))
# print(len(album_song))

# higest rating song
# highest_rating=[song["rating"] for song in data]
# print(max(highest_rating))
# top_song=reduce(lambda s1,s2:s1 if s1["rating"]>s2["rating"] else s2,data)
# print(top_song)

# sad mode songs with random sample of 2
# sad_song=[song for song in data if song["mode"]=="sad"]
# print(random.sample(sad_song,2))

# total number of albums
# total_album=set([s["album"] for s in data ])
# print(len(total_album))

# wich album containg most songs
sn_count={}
for song in data:
    album_name=song.get("album")
    if album_name in sn_count:
        sn_count[album_name]+=1
    else:
        sn_count[album_name]=1
print(sn_count)

most_song=max(sn_count.items(),key=lambda s:s[1])
print(most_song)