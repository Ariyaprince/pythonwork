class Employee:
    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.id=kwargs.get("id")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.name


emp=Employee(name="ram",id=10,role="hr")
# print(emp)

class Department:
    def __init__(self,**kwargs):
        employ=kwargs.get("employee")
        if employ.role=="admin":
            self.deprt_name=kwargs.get("deprt_name")
            self.employee=kwargs.get("employee")
        else:
            print("no access")

        self.deprt_name=kwargs.get("deprt_name")
        self.employee=kwargs.get("employee")
    def __str__(self):
        return self.deprt_name

department=Department(deprt_name="developer",employee=emp)


# print(department)

