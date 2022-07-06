lst=[1,2,3,9]
squares=list(map(lambda n:n**2,lst))
print(squares)

cubes=list(map(lambda n:n**3,lst))
print(cubes)

# num-1 if <5,num+1 if >5

out=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(out)