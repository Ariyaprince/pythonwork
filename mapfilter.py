# lst=[1,2,3,9]
# squares=list(map(lambda n:n**2,lst))
# print(squares)
#
# cubes=list(map(lambda n:n**3,lst))
# print(cubes)
#
# # num-1 if <5,num+1 if >5
#
# out=list(map(lambda n:n-1 if n<5 else n+1,lst))
# print(out)

from functools import reduce
lst=[1,2,3,4]
# even=list(filter(lambda n:n%2==0,lst))
# print(even)
#
# gt_three=list(filter(lambda n:n>3,lst))
# print(gt_three)


sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)

prdct=reduce(lambda n1,n2:n1*n2,lst)
print(prdct)

maximum=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(maximum)

minimum=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(minimum)


