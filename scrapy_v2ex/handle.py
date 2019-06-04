import re
import requests
from  multiprocessing import Process


def get_href(content):
    res = []
    for q in content.split("</a>"):
        re_ = re.findall(re.compile(r'<a href="(.*)">(.*)'),q)
        try:
            if re.findall(re.compile(r"深圳"),re_[0][1]) and re.findall(re.compile(r"ython"),re_[0][1]):
                res.append(re_[0])
        except IndexError as e:
            continue
    return res

def get_details(urls,ress):
    print("start handling %s"%(urls))
    results = []
    res = requests.get(urls)
    reg = re.compile(r'''(
    ([a-zA-Z0-9._%+-]+)
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    (\.[a-zA-Z]{2,4})?
    )''',re.VERBOSE)
    for group in reg.findall(res.text):
        for li in range(len(group)):
            results.append(group[li])
    ress.extend(results)

f = open("data/001.html","r")
lines = f.readlines();
f.close()
print("there are %d items"%(len(lines)))

results = []
for li in lines:
    results.extend(get_href(li))

print("there are %d items "%(len(results)))

ress = []
#for li in results:
#    ress.extend(get_details('https://www.v2ex.com'+li[0]))

for li in range(len(results)):
    _p = Process(target=get_details,args=('https://www.v2ex.com'+results[li][0],ress,))
    _p.start()

print("there are %d emails "%(len(ress)))

with open ("data/emails.txt","a+",encoding='utf-8') as f:
    for emlitem in ress:
        f.write(emlitem)

