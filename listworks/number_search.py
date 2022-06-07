arr=[10,11,12,13,14,15,16,17]
element=154
flag=0
for num in arr:
    if element==num:
        flag=1
        break
print("element found" if flag==1 else "not found")
