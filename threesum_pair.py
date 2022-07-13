lst=[3,4,5,6,2]
# 3 sum pair 9 [4,3,2]
# 3 sum pair 12 [3,4,5],[6,4,2]

sum=8
res=[]

def pairs(lst,sum):
    while lst:
        num=lst.pop()
        diff=sum-num
        if diff in lst:
            res.append((diff,num))
    return res
print(pairs(lst,sum))
