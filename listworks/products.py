mobiles=[
    [1000,"samsungA52","4g","AMOLED",27000,"samsung",12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung",20],
    [1002, "redminote10", "4g", "led", 17000, "redmi",50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi",70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung",1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung",34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung",7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung",89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung",0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple",0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus",67]

]

# no of mobiles
# print(f"total={len(mobiles)}")
#
#  total out of stock
# out_of_stock=[mob for mob in mobiles if mob[-1]==0]
# print(out_of_stock)

# total stock
# avl_stock=[mob[-1] for mob in mobiles]
# print(sum(avl_stock))

# mobiles available between 20000 and 30000
# mobil_gt=[mob for mob in mobiles if mob[4] in range(20000,30001)]
# print(mobil_gt)

# print 5g mobiles
# mobiles_fiveg=[mob for mob in mobiles if mob[2]=="5g"]
# print(mobiles_fiveg)

# costly mobiles
# mobiles.sort(reverse=True,key=lambda mob:mob[4])
# print(mobiles)

# costly_mobile=max(mobiles,key=lambda m:m[4])
# print(costly_mobile)

# is there any mobile available at 10000
mobile_ten=[mob[4]==27000 for mob in mobiles]
print("available" if True in mobile_ten else "not available")