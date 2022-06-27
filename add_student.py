class Course:
    def post(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")

class Batch:
    def post(self,**kwargs):
        self.b_code=kwargs.get("b_code")
        self.b_name=kwargs.get("b_name")
        self.course=kwargs.get("course")

class Student:
    def post(self,**kwargs):
        s_name=kwargs.get("st_name")
        if s_name.course=="python":

            self.st_name=kwargs.get("st_name")
            self.roll=kwargs.get("roll")
            self.batch=kwargs.get("batch")
        else:
            print("no")


crs=Course(course_name="python",status=True)
bth=Batch(b_code=212,b_name="may22",course=crs)
stu=Student(st_name="ariya",roll=2,batch=bth)
