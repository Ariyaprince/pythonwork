from functools import reduce
lst=[8,34,78,9]
str_lst=[str(n) for n in lst]
str_list=sorted(str_lst,reverse=True)
out=reduce(lambda n1,n2:(n1+n2) if (n1+n2)>(n2+n1) else (n2+n1),str_list)
print(out)