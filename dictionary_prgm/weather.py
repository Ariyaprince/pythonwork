weather=[
    {"district": "tvm", "temp":30},
    {"district": "ktm","temp":28 },
    {"district": "apy","temp":27},
    {"district": "idk","temp":18 },
    {"district": "ekm","temp":31 },
    {"district": "pta","temp":21},
    {"district": "tsr","temp":24},
    {"district": "kzd","temp":29},
    {"district": "pkd","temp":34},
    {"district": "mpm","temp":31},
    {"district": "tvm", "temp": 31},
    {"district": "ktm", "temp": 29},
    {"district": "apy", "temp": 26},
    {"district": "idk", "temp": 20},
    {"district": "ekm", "temp": 30},
    {"district": "pta", "temp": 22},
    {"district": "tsr", "temp": 27},
    {"district": "kzd", "temp": 28},
    {"district": "pkd", "temp": 30},
    {"district": "mpm", "temp": 29},

]
out={}
for data in weather:
    dist_name=data["district"]
    curr_temp=data["temp"]
    if dist_name in out:
        old_temp=out[dist_name]
        if curr_temp>old_temp:
            out[dist_name]=curr_temp

    else:
        out[dist_name]=curr_temp
print(out)

# sort out based on temparature
sorted_temp=sorted(out.items(),key=lambda item:item[1],reverse=True)
print(sorted_temp)

# find max tem district
max_temp=max(out,key=lambda item:item[1])
print(max_temp)


# find min tem district

# dictionary methods