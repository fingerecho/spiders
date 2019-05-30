import requests
import os
from yaml import full_load as load

data_path = os.path.join(".","data")
url_sample = "https://www.v2ex.com/go/jobs?p={id}"
yaml_config = os.path.join(".","headers.yaml")


def change_headers(func):
    def wrapper():
        tar = func(h);print("in wrapper",tar)
        #tar.update({":authority":"www.v2ex.com"})
        #tar.update({":method":"GET"})
        #tar.update({":path":"/go/jobs?p=1"})
        #tar.update({":scheme":"https"})
        tar.update({"upgrade-insecure-requests": "2"})
    return wrapper


#@change_headers
def init_headers(**headers):
    with open(yaml_config,"r",encoding='utf-8') as f:
        src = f.read()
        headers = load(src)
    return headers
 
def get_one(url,saving):
    res = requests.get(url,headers=init_headers())
    if res.status_code == 200:
        #print(len(res.text.split("\n")))
        src = res.text.split("\n")[328:-75]
        with open(saving,"a+",encoding='utf-8') as f:
            for lin in src:
                f.write(lin)
    else:
        print("error on this url :",url)
        print("status code is ",res.status_code)

def get_all(start_pages,end_pages,pages_count,saving,func=get_one):
    for i in range(start_pages,end_pages+1):
        func(url_sample.format(id=str(i)),saving)
        print("scrapyed the {id} pages ".format(id=str(i)))
if __name__ == "__main__":
    print("the last",init_headers())
    get_all(54,1729,1729,os.path.join(data_path,"001.html"))
