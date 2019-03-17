import scrapy


class YelpSpider(scrapy.Spider):
    name = 'yelp_items'

    def start_requests(self):
        urls = [
                'https://www.yelp.com/search?find_desc=&find_loc=sunyvale%2C+ca&ns=1',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Handle response from request
        main_content = response.xpath('//div[contains(@class, "mainContentContainer")]')
        item_list = main_content.xpath('.//li[contains(@class, "list-item")]')
        for item in item_list:
            yield {
                    'name': item.xpath('.//a/text()').get(),
                    'address': item.xpath('.//address[contains(@class, "address")]//span/text()').get(),

                    }
            return
