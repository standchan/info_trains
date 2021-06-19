import scrapy


class HuochepiaoSpider(scrapy.Spider):
    name = 'huochepiao'
    base_domain = 'huochepiao.com'
    base_url = "http://search.huochepiao.com/checi/D1"

    allowed_domains = [base_domain]
    start_urls = [base_url]

    # def parse(self, response):
    #     filename = "D4.html"
    #     # open(filename,'w+').write(response.body)
    #     with open('D4.html','wb') as f:
    #         f.write(response.text)
    #         f.close()

    def parse2(self,response):
        print(response.content)
        pass
