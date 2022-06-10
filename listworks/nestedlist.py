lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]
# for sub_lst in lst:
#     for num in sub_lst:
#         if num>16:
#             print(num)


# flatten_lst=[]
# for sub_lst in lst:
#     for num in sub_lst:
#         flatten_lst.append(num)
# print(flatten_lst)
# print(max(flatten_lst))

# list comprhension

flatten_lst=[num for sub_lst in lst for num in sub_lst]
print(flatten_lst)
# flatten_lst.sort()
# print(flatten_lst)
#
# num_gt_sixteen=[num for num in flatten_lst if num>16 ]
# print(num_gt_sixteen)

# odd_num_lst=[num for num in flatten_lst if num%2!=0]
# print(odd_num_lst)

# even_num=[num for num in flatten_lst if num%2==0]
# print(sum(even_num)

flatten_lst=[num for sub_lst in lst for num in sub_lst]
# for num in flatten_lst:
#     if num>25:
#         print(num+1)
#     elif num<25:
#         print(num-1)

mapped_list=[num+1 if num>25 else num-1 for num in flatten_lst]
print(mapped_list)
