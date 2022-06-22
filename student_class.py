class Student:
    name:str
    roll_no:int
    course:str
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course
    def print_student(self):
        print(self.name,self.roll_no,self.course)
s1=Student("ariya",6,"python")

s1.print_student()

