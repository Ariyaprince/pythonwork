# for row in range(1,5):
#     for col in range(1,4):
#         print(row,end="")
#     print()



# for row in range(1,5):
#     for col in range(1,row+1):
#         print(row,end=" ")
#     print()


# for row in range(1,5):
#     for col in range(1,row+1):
#         print("#",end=" ")
#     print()


for r in range(1,5):
    for c in range(5,r,-1):
        print("#",end=" ")
    print()

