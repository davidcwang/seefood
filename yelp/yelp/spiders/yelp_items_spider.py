import scrapy


class YelpSpider(scrapy.Spider):
    name = 'yelp_items'

    def start_requests(self):
        urls = [
                'https://www.yelp.com/biz_photos/dishdash-sunnyvale?start=0',
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Handle response from request
        photo_links = response.xpath('//img[@class="photo-box-img"]').xpath('@src').getall()
        return
