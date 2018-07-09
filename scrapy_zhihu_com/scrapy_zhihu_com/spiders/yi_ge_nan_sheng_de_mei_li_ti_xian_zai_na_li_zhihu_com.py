import scrapy , os

class DmozSpider(scrapy.Spider):
    name = "yi_ge_nan_sheng_de_mei_li_ti_xian_zai_na_li"
    allowed_domains = ["zhihu.com"]
    start_urls = [
        "https://www.zhihu.com/question/266276255",
    ]

    def parse(self, response):
        content = response.xpath('//*[@class="List-item"]')
                                ##//*[@id="QuestionAnswers-answers"]/div/div/div[2]/div/div[2]/div/div[2]/div[1]
        print(len(content))
        print(content[0].extract())
        print(content[1].extract())
        #with open(self.name, 'xb') as f:
        #    f.write(content)