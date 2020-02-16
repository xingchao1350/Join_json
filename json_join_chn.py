import json
from os import listdir
path = 'd:/python/code/t1/join'
dirs = listdir(path)
print(dirs)
join_res=[]
for i in range(len(dirs)):
    with open('d:/python/code/t1/join/'+dirs[i], 'r', encoding='utf-8') as f:
        join_temp = json.load(f)
        join_res.extend(join_temp)
with open('d:/python/code/t1/result/data1.json', 'w', encoding='utf-8') as f:
    json.dump(join_res, f, ensure_ascii=False)