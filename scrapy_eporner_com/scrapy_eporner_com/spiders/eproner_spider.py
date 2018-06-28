import scrapy


class mingyan(scrapy.Spider):  # 需要继承scrapy.Spider类

    name = "fuck"  # 定义蜘蛛名Wx`
    start_urls = [
        'https://www.eporner.com/',
    ]

    def parse(self, response):
        '''
        start_requests已经爬取到页面，那如何提取我们想要的内容呢？那就可以在这个方法里面定义。
        这里的话，并木有定义，只是简单的把页面做了一个保存，并没有涉及提取我们想要的数据，后面会慢慢说到
        也就是用xpath、正则、或是css进行相应提取，这个例子就是让你看看scrapy运行的流程：
        1、定义链接；
        2、通过链接爬取（下载）页面；
        3、定义规则，然后提取数据；
        就是这么个流程，似不似很简单呀？
        '''


        #urls=response.xpath('//*[@id="div-search-results"]/div[9]/div/a/@href')
        urls = response.xpath('//*[@class="mb"]/a/@href')
        urls_0 = urls.extract()
        with open("./scrapy_eporner_com/data/valid_urls.md","a+",encoding="utf-8") as f:
            for i in urls_0:
                f.write(i)
                f.write("\n")
        self.log("valid urls is %d"%(len(urls_0)))
        if len(urls_0)>=1:
            self.log(urls_0[0])
            self.log(len(urls_0))

        next_page = response.xpath('//a[@title="Next page"]/@href').extract()
        self.log(next_page)
        if   next_page is not None:
            next_page = response.urljoin(next_page[0])
            self.log(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        """
        filename = 'mingyan-%s.html' % page  # 拼接文件名，如果是第一页，最终文件名便是：mingyan-1.html
        with open(filename, 'wb') as f:  # python文件操作，不多说了；
            f.write(response.body)  # 刚才下载的页面去哪里了？response.body就代表了刚才下载的页面！
        self.log('保存文件: %s' % filename)  # 打个日志

        """
"""
def start_requests(self):  # 由此方法通过下面链接爬取页面

    # 定义爬取的链接
    urls = [
        'http://lab.scrapyd.cn/page/1/',
        'http://lab.scrapyd.cn/page/2/',
    ]
    for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)  # 爬取到的页面如何处理？提交给parse方法处理
"""

