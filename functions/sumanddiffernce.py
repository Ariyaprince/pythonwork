# def add_numbers(n1,n2):
#     return n1+n2
# print(add_numbers(10,20))
#
# def sub_numbers(n1,n2):
#     return n1-n2
# print(sub_numbers(20,10))
#
# def smart_sub(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1
# print(smart_sub(5,10))
#
# def num_check(num):
#     return "even" if num%2==0 else "odd"
# print(num_check(3))

# def validate_gmail(email):
#     return email.endswith("@gmail.com")
# print(validate_gmail("ariya@gmail.com"))

def prime(num):

    for i in range(2,num):
        return "true" if num%i!=0 else "false"
print(prime(4))


# cube=lambda n:n**3
# print(cube(3))
#
#
# smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
# print(smart_sub(2,5))




