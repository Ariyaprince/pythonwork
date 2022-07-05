students=open("students.txt")
all_students=[s.rstrip("\n") for s in students]
print(all_students)

failed_students=open("failed.txt")
f_students=[f.rstrip("\n") for f in failed_students]
print(f_students)

passed_students=open("passed_studentd","w")
p_students=set(all_students)-set(f_students)
print(p_students)
for p in p_students:
    p+="\n"
    passed_students.write(p)