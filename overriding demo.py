# class Parent:
#     def properties(self):
#         self.props={"mobil":"iphone","bike":"passion"}
#         return self.props
# class Child(Parent):
#     def properties(self):
#         props=super(Child, self).properties()
#         props["car"]="swift"
#         return props
# ch=Child()
# print(ch.properties())


class Editor:
    def functionalities(self):
        self.func=["createnewfile","excecute","save"]
        return self.func

class Pycharm(Editor):
    def functionalities(self):
        func=super(Pycharm, self).functionalities()
        func.append(["ebug","versioncontrol"])
        return func
pyc=Pycharm()
print(pyc.functionalities())