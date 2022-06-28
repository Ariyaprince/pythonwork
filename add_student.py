class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")
    def __str__(self):
        return self.course_name
django=Course()
django.add_course(course_name="python",status=True)
bigdata=Course()
bigdata.add_course(course_name="bigdata",status=True)
print(django)
print(bigdata)
class Batch:
    def add_batch(self,**kwargs):
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")
        self.course=kwargs.get("course")
    def __str__(self):
        return self.batch_code
db1=Batch()
db1.add_batch(batch_code="djmay22",start_date="5-5-2022",course=django)
bd1=Batch()
bd1.add_batch(batch_code="bdmay22",start_date="15-5-2022",course=bigdata)
print(db1)
print(bd1)

class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.gender=kwargs.get("gender")
        self.roll=kwargs.get("roll")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name
rahul=Student()
rahul.add_student(student_name="rahul",gender="male",roll=20,batch=db1)
akshay=Student()
akshay.add_student(student_name="akshay",gender="male",roll=25,batch=db1)
print(akshay)
ariya=Student()
ariya.add_student(student_name="ariya",gender="female",roll=30,batch=bd1)
print(rahul.batch.course)



