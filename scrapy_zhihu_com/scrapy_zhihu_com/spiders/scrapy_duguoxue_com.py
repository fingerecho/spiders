# -*- coding: utf-8 -*-
import scrapy
import os
from ..settings import MY_DOWNLOADS_FILE


class ScrapyDuguoxueComSpider(scrapy.Spider):
    name = 'scrapy_duguoxue_com'
    allowed_domains = ['duguoxue.cn']

    def start_requests(self):
        url = 'http://duguoxue.cn/yuedu/'
        yield scrapy.Request(url ,callback=self.pare)

    def pare(self, response):
        ##content= response.xpath("/html/body/div[5]").extract() ###/html/body/div[5]
        ##self.log(len(content))   /html/body/div[5]/div[9]/strong
        ### 山海经   /html/body/div[5]/div[1]/a   /html/body/div[5]/div[1]/strong/a
        dest_xp = response.xpath('/html/body/div[5]/div/strong/a')  #/html/body/div[5]/div[1]/a
        text_url = dest_xp.xpath('@href').extract()
        self.log(len(text_url))
        book_name = dest_xp.xpath('text()').extract()
        self.log(book_name)
        #for i in content:
        #    self.log(i)
        path__= os.path.join(MY_DOWNLOADS_FILE,"book_from_duguoxue_com")
        for item in range(len(text_url)):
            if  os.path.exists(os.path.join(path__,book_name[item])):
                continue
            self.log(book_name[item]+"    "+text_url[item])
            meta_dict = {}
            meta_dict['book_name']=str(book_name[item])
            yield scrapy.Request(text_url[item],meta=meta_dict,callback=self.scrapy_mulu)
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
            self.log("-----------------get %s detail_ mulu  ----------------"%title_)
            self.log("----------------url is %s --------------------"%detail_url[item])
            #cookies_ = response.cookies.get_dict()
            """zh_choose=n; 
            Hm_lvt_26fa54d2ec1868fdbfa4888a1a216af1=1531132126;
            Hm_lpvt_26fa54d2ec1868fdbfa4888a1a216af1=1531151813"""
            cookies_={"zh_choose":"n",
            "Hm_lvt_26fa54d2ec1868fdbfa4888a1a216af1":"1531132126",
            "Hm_lpvt_26fa54d2ec1868fdbfa4888a1a216af1":"1531151813"}
            yield  scrapy.Request(detail_url[item],meta=title_dict,cookies=cookies_,callback=self.scrapy_detail_,dont_filter=True)
    def scrapy_detail_(self,resposne):
        title = resposne.meta['title']
        book_name = resposne.meta['book_name']
        detail=resposne.xpath('/html/body/article/p/text()').extract()
        self.log(detail)
        path__= os.path.join(MY_DOWNLOADS_FILE,"book_from_duguoxue_com",book_name)
        if not os.path.exists(path__):
            os.makedirs(path__)
        paa = os.path.join(path__, '%s.txt' % (title))
        #self.log("start write the %s  of %s  on %s"%( title,book_name,paa))
        with open(paa,"a+",encoding="utf-8") as f:
            f.writelines(detail)
        pass

