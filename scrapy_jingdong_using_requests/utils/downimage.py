#!/usr/bin/python

import requests,os

def random_str(param: object) -> object:
    pass

def img_download(imgurl,count):
    file_name = "../Images/" + str(count) + ".jpg"
    img = requests.get(imgurl)
    with open(file_name, "wb") as f:
        for chunk in img.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()
    print("download image succeed")
