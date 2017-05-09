import os

#url ./../sql/mobile.sql

def createFile(url,content):
    count=0
    with open(url,'a') as f:
        f.write("INSERT INTO mobile_basic(mb_id,mb_desc ,mb_img_addr)VALUES")
        for i in content:
            if count!=len(content)-1:
                f.write(i+",")
            else:
                f.write(i)
            count=count+1
        f.write(";\r\n\r\n")


