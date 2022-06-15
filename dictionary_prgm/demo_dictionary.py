student={"name":"ariya","roll no":20,"class":7,"division":"a","mark":25}
# print(student["name"])
# print(student["class"])
# print(student["division"])
# print("school" in student)
# student["school"]="toch"
# print(student)
# student["mark"]=20
# print(student)
# student["roll no"]=30
# print(student)

# print(student.get("name"))
# print(student.get("roll no"))

# if "school" in student:
#     student["school"]="abc"
#
# else:
#     student["school"]="toch"
# print(student)

# mark>20,mark-10,else mark-5

if student["mark"]>20:
    student["mark"]-=10
else:
    student["mark"]-=5
print(student)
