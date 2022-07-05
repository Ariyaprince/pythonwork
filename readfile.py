# f=open("abc.txt")
# for line in f:
#     print(line)

# lines=list(f)
# print(lines)

# lst=[line.rstrip("\n") for line in f]
# print(lst)

f=open("abc.txt","w")
# c_name="luminar"
# f.write(c_name)

lst=["python","java","angular"]
for lang in lst:
    lang+="\n"
    f.write(lang)





