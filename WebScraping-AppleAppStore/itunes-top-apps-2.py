# Run with
#
#   scrapy runspider a3-akankshr-itunes-topapps-2.py –t csv –o -> a3-akankshr-itunes-topapps-2.csv

# Akanksha Rawat

from scrapy.spiders import Spider
from scrapy import Request


class S1(Spider):
    name = 's1'
    
    start_urls = ["http://www.apple.com/itunes/charts/free-apps/"]
    custom_settings = { 'DOWNLOAD_DELAY': 0.5 }
    
    def parse(self, response):
        
        rows = response.xpath('//div[@id = "main"]/section/div/ul/li')
        items = []
        for row in rows:
            item = {}
            item['Name'] = row.xpath("./h3/a/text()").extract()
            item['Category'] = row.xpath("./h4/a/text()").extract()
            item['appstore_link_url'] = row.xpath("./h3/a/@href")[0].extract()
            item['img_src_url']=row.xpath("./a/img/@src").extract()
            url = item['appstore_link_url']
            
            req = Request(url, callback = self.parse_2)

            req.meta['data'] = item
            items.append(req)
        return items

    def parse_2(self, response):
        
        item = response.meta['data']
        data = response.xpath('.//figcaption[@class="we-rating-count star-rating__count"]/text()')[0].extract()

        
        item['Star_Rating'] = data.split(',')[0]
        item['Num_Rating'] = data.split(',')[1]
               
        return item
        

