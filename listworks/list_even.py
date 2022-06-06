# numbers=[12,13,3,5,6,8,9,10]
# for num in numbers:
#     if num%2==0:
#         print(num)



# numbers=[12,13,14,15,16,17,18]
# for num in numbers:
#     if num>15:
#
#         print(num+1)
#     elif num<15:
#         print(num-1)
#     elif num==15:
#         print(num)

#print count of numbers where numbers in range 0f 14 to 18

# numbers=[12,13,14,15,16,17,18]
# count=0
# for num in numbers:
#
#     if num>=14 and num<=18:
#         count+=1
# print(count)

# numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
# count_p=0
# count_n=0
# count_zero=0
#
# for num in numbers:
#     if num>0:
#         count_p+=1
#
#     elif num<0:
#         count_n+=1
#     elif num==0:
#         count_zero+=1
# print(f"positive={count_p},negative={count_n},zero={count_zero}")



numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
sum=0
for num in numbers:
    sum=sum+num
    num+=1
print(sum)




