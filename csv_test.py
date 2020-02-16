import csv
f=open('01.csv','r')
table=csv.reader(f)
for i in table:
    print(i)
