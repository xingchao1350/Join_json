import json                             #系统自带
from os import listdir                  #系统自带，获取当前目录
path = 'd:/python/code/t1/join'         #指定目录
dirs = listdir(path)                    #获取当前目录列表
print(dirs)
join_res=[]                             #定义空列表
for i in range(len(dirs)):
    with open('d:/python/code/t1/join/'+dirs[i], 'r', encoding='utf-8') as f:   #循环读取当前目录下json文件
        join_temp = json.load(f)                                                #赋值给临时列表
        join_res.extend(join_temp)                                              #用expand方法追加列表
with open('d:/python/code/t1/result/data1.json', 'w', encoding='utf-8') as f:   #以写入为目的打开文件
    json.dump(join_res, f, ensure_ascii=False)                                  #写入文件，写入前会清空当前文件