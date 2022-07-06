# error handling
#
# try-->doubtful code,block
# except-->how to handle error,block
# raise-->keyword,custom error throw eg invalid age-given by user
# finally-->block,clean up processing

# num1=int(input("enter num1="))
# num2=int(input("enter num2="))

# try:
#     res=num1/num2
#     print(res)
# except Exception as e:
#     print(e)
#
# print("line1")
# print("line2")

# try:
#     res=num1/num2
#     print(res)
# except Exception as e:
#     num2=int(input("enter num2="))
#     res=num1/num2
#     print(res)
#
# finally:
#     print("line1")
#     print("line2")

# age=int(input("enter number="))
# if(age<18):
#     raise Exception("not eligible for booster dose")
# else:
#     print("eligible")

phone=input("enter num=")
if len(phone)!=10:
    raise Exception("invalid")
else:
    print("valid")