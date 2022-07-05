import json
with open("countries.json",encoding="utf") as f:
    data=json.load(f)

# print total number of country details
print(len(data))


# print languages of ukraine
ukrn_lan=[country["languages"] for country in data if country["name"]=="Ukraine"]
for lan in ukrn_lan[0]:
    print(lan["name"])
print(ukrn_lan)


# print currency of palestine
cur_china=[country["currencies"] for country in data if country["name"].lower().startswith("india")]
print(cur_china)
currency_name=[name["name"] for name in cur_china[0]]
print(currency_name)


# print population of india
pop_ind=[country["population"] for country in data if country["name"]=="India"]
print(pop_ind)


# print neighbouring countries of australia
astr=[country for country in data if country["name"]=="Australia" ]
print(astr)


# print neighbouring country names of India
def get_country(country_name):
    return [country for country in data if country["name"].lower().startswith(country_name)]
india_data=get_country("india")
borders=india_data[0].get("borders")
sharing_borders=[country["name"] for country in data if country["alpha3Code"] in borders]
print(sharing_borders)


# highest population
highest_pop=max(data,key=lambda i:i.get("population"))
print(highest_pop["name"])


# lowest population
lowest=min(data,key=lambda i:i.get("population"))
print(lowest["name"])


