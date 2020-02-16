import csv              #系统自带
f=open('01.csv','r')    #以读取的目的打开文件
table=csv.reader(f)     #读取文件并赋值给table列表
for i in table:
    print(i)            #遍历元素
