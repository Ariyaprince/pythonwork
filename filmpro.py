# no.of movies released in 2022

movies=open("films.txt")
movie=[m.rstrip("\n").split(",") for m in movies]
print(movie)

# film_22=[mov for mov in movie if mov[1]=="2022" ]
# print(film_22)
# print(len(film_22))
# num=0
# for mov in movie:
#     if mov[3]=="malayalam":
#         num+=1
# print(num)

# film_mal=[mov for mov in movie if mov[3]=="malayalam"]
# print(len(film_mal))

#
# film_theatre=[mov for mov in movie if mov[-1]=="theater"]
# print(film_theatre)
#
# greater_rating=[m for m in movie if m[2]>"4"]
# print(greater_rating)

# {2022:4,2021:6,2020:2}, max=2021
movie_out={}
for m in movie:
    year=m[1]
    if year in movie_out:
        movie_out[year]+=1
    else:
        movie_out[year]=1
print(movie_out)

out=max(movie_out.items(),key=lambda i:i[1])
print(out)

