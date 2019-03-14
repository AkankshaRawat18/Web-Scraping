# Run with
#
# scrapy runspider a3-akankshr-itunes-topapps-1.py –t csv –o -> a3-akankshr-itunes-topapps-1.csv

# Akanksha Rawat

from scrapy.spiders import Spider

class S1(Spider):
    name = 's1'
    # allowed_domains = ['craigslist.org']
    start_urls = [ "http://www.apple.com/itunes/charts/free-apps/" ]
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

            items.append(item)
        return items