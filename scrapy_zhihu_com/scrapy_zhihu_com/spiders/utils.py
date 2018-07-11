from ghost import Ghost
import re
class Cookieutil:
    def __init__(self,url):
        #log.msg('init cookieutil class ,will be get %s cookie information!' %url,log.INFO)
        gh = Ghost()
        gh.open(url)
        gh.open(url)
        gh.save_cookies("cookie.txt")
        gh.exit()
    def getCookie(self):
        cookie = ''
        with open("cookie.txt") as f:
            temp = f.readlines()
            for index in temp:
                cookie += self.parse_oneline(index).replace('\"','')
        return cookie[:-1]
    def parse_oneline(self,src):
        oneline = ''
        if re.search("Set-Cookie",src):
            oneline = src.split(';')[0].split(':')[-1].strip()+';'
        return oneline


class transCookie(object):
    def __init__(self, cookie):
        self.cookie = cookie

    def stringToDict(self):
        itemDict = {}
        items = self.cookie.split(';')
        for item in items:
            key = item.split('=')[0].replace(' ', '')  # 记得去除空格
            value = item.split('=')[1]
            itemDict[key] = value
        return itemDict
