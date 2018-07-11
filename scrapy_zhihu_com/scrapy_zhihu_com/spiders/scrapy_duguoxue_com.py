# -*- coding: utf-8 -*-
import scrapy
import os
from ..settings import MY_DOWNLOADS_FILE
from  .utils import  Cookieutil ,transCookie
import time

#COOKIE_STR = "Hm_lvt_30664cf450dbb4c875787214ae29c091=1531210756,1531232839; Hm_lpvt_30664cf450dbb4c875787214ae29c091=1531232839; hdgg_uid=uid_0710_2476f192-10e9-4c40-8663-632984f91e2b; gr_user_id=cb42d3cf-d153-4517-aa61-fe050053b354; gr_session_id_bdd0f83d74ae607c=33a173e0-3169-4df9-9d07-f4d9e51638ec; gr_session_id_bdd0f83d74ae607c_33a173e0-3169-4df9-9d07-f4d9e51638ec=true"
#COOKIE_STR = "zh_choose=n; Hm_lvt_26fa54d2ec1868fdbfa4888a1a216af1=1531151900; zh_choose=n; Hm_lvt_787549918fa5b89b877a8e0195adbac4=1531210946; Hm_lpvt_787549918fa5b89b877a8e0195adbac4=1531210946; Hm_lpvt_26fa54d2ec1868fdbfa4888a1a216af1=1531232827"
COOKIE_STR = "zh_choose=n; Hm_lvt_26fa54d2ec1868fdbfa4888a1a216af1=1531151900; zh_choose=n; Hm_lvt_787549918fa5b89b877a8e0195adbac4=1531210946; Hm_lpvt_787549918fa5b89b877a8e0195adbac4=1531210946; Hm_lpvt_26fa54d2ec1868fdbfa4888a1a216af1=1531237472"
class ScrapyDuguoxueComSpider(scrapy.Spider):
    begin_time = time.time()
    name = 'scrapy_duguoxue_com'
    allowed_domains = ['duguoxue.cn']
    headers={
        'User-Agent':'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
    }

    def start_requests(self):
        url = 'http://duguoxue.cn/yuedu/'
        self.__cookie = transCookie(COOKIE_STR).stringToDict()
        yield scrapy.Request(url ,cookies=self.__cookie,callback=self.pare)

    def pare(self, response):
        ##content= response.xpath("/html/body/div[5]").extract() ###/html/body/div[5]
        ##self.log(len(content))   /html/body/div[5]/div[9]/strong
        ### 山海经   /html/body/div[5]/div[1]/a   /html/body/div[5]/div[1]/strong/a
        dest_xp = response.xpath('/html/body/div[5]/div/strong/a')  #/html/body/div[5]/div[1]/a
        text_url = dest_xp.xpath('@href').extract()
        book_name = dest_xp.xpath('text()').extract()
        for item in range(len(text_url)):
            #if  os.path.exists(os.path.join(path__,book_name[item])):
            #    continue
            meta_dict = {}
            meta_dict['book_name']=str(book_name[item])
            yield scrapy.Request(text_url[item],cookies=self.__cookie,meta=meta_dict,callback=self.scrapy_mulu)
        pass
    def scrapy_mulu(self,response):
        ###/html/body/ul/li[3]/a
        info = response.xpath('/html/body/ul/li/a')
        detail_url = info.xpath('@href').extract()
        detail_title = info.xpath('@title').extract()
        for item in range(0,len(detail_url)):
            self.log(detail_title[item]+"   "+detail_url[item])
            title_ = str(detail_title[item])
            title_dict = {}
            title_dict['title']=title_
            title_dict.update(response.meta)
            #self.headers['Cookie'] = Cookieutil(detail_url[item]).getCookie()
            yield  scrapy.Request(detail_url[item],meta=title_dict,cookies=self.__cookie,callback=self.scrapy_detail_,dont_filter=False)
        pass
    def scrapy_detail_(self,resposne):
        self.log("start this detail_wwwwwwwwww ")
        detail=resposne.xpath('/html/body/article/p/text()').extract()
        book_name = resposne.meta['book_name']
        title = resposne.meta['title']
        path__ = os.path.join(MY_DOWNLOADS_FILE, "book_from_duguoxue_com")
        path__ = os.path.join(path__, book_name)
        paa =os.path.join(path__,"%s.txt"%(title))
        if not os.path.exists(path__):
            os.makedirs(path__)
        if os.path.exists(paa):
            self.log(" ---------%s  is exists  ----------"%paa)
            return
        else:
            self.log("-------------------------------file name is %s-------------------------------------------" % paa)
        #self.log(detail)
        self.log("start this writing file of %s" % paa)
        self.log("detail is %s"%("".join(detail)))
        with open(paa,"a+",encoding="utf-8") as f:
            f.writelines(detail)
        pass

