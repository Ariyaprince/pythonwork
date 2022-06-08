# lst1=[10,11,12,13,14,14,14]
# dup_list=[]
# for i in range(0,len(lst1)):
#     for j in range((i+1),len(lst1)):
#         if lst1[i]==lst1[j]:
#             dup_list.append(lst1[i])
# print(f"first recurssive is {dup_list[0]} and 2nd recursive is {dup_list[1]}")


lst=[2,3,4,6,5]
sum=8
for i in range(0,len(lst)):
    for j in range((i+1),len(lst)):
        cur_sum=lst[i]+lst[j]
        if sum==cur_sum:
            print(f"pairs are {lst[i]},{lst[j]}")
            break