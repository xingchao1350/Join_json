import json
with open('beer_doctor.json', 'r',encoding='utf-8') as f:
    d1 = json.load(f)
with open('chuipi.json', 'r',encoding='utf-8') as f:
    d2 = json.load(f)
d1.extend(d2)
with open('data1.json', 'w',encoding='utf-8') as f:
    json.dump(d1, f,ensure_ascii=False)