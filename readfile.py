f=open("abc.txt")
# for line in f:
#     print(line)

# lines=list(f)
# print(lines)

lst=[line.rstrip("\n") for line in f]
print(lst)



