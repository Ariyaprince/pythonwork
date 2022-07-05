mobiles=open("mobiles.txt")
mobile=[mob.rstrip("\n").split(",") for mob in mobiles]
print(mobile)



# all_mobiles=[]
# for line in mobiles:
#     mobile=line.rstrip("\n").split(",")
#     all_mobiles.append(mobile)
# print(all_mobiles)
# max_mob=max(all_mobiles,key=lambda m:int(m[2]))
# print(max_mob)

fiveg=[m for m in mobile if m[3]=="4g"]
print(fiveg)
