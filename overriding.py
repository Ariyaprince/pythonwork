# overriding

class Parent:
    def phone(self):
        print("nokia")
    def bike(self):
        print("passion")
class Child(Parent):
    def phone(self):
        print("iphone")
    def bike(self):
        print("duke")
ch=Child()
ch.phone()
ch.bike()