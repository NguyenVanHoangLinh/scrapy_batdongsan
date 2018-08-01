import scrapy
from ..items import real_estateItem
from scrapy.utils.markup import remove_tags
from scrapy_splash import SplashRequest
from datetime import datetime as dt
class RealEstateSpider(scrapy.Spider):
    name = "estate"
    def start_requests(self):
        yield SplashRequest(
            url='https://batdongsan.com.vn/nha-dat-ban/p1',
            callback=self.parse,
        )
    

    def parse(self, response):
        # follow links to estate page
        for href in response.css('div.p-title h3 a::attr(href)').extract():
            yield SplashRequest(response.urljoin(href), self.parse_estate)

        # follow pagination links
        next_page_url = response.css('div.background-pager-right-controls a:nth-last-child(3)::attr(href)').extract_first()
        if next_page_url is not None:
            next_page_url=response.urljoin(next_page_url)
            yield scrapy.Request(next_page_url,callback=self.parse)

    def parse_estate(self, response):
        def extract_with_css(query):
            try:
                result = response.css(query).extract_first().strip()
            except:
                result = ""
            return result
        estate_title = extract_with_css('h1[itemprop="name"]::text')
        estate_address = extract_with_css('div.table-detail div.row:nth-child(2) div.right::text')
        estate_price = extract_with_css('span.gia-title strong::text')
        estate_area = extract_with_css('span.gia-title:nth-child(2) strong::text')
        description = response.css('div.pm-desc::text').extract()
        estate_description=' '.join(description).strip()
        estate_tag = response.css('div.tagpanel a::text').extract()
        estate_type = extract_with_css('div.table-detail div.row:nth-child(1) div.right::text')
        date = response.css('div.prd-more-info div:nth-child(3)::text').extract()
        estate_date = ' '.join(date).strip()
        # expired_date = response.css('div.prd-more-info div:nth-child(4)::text').extract()
        # estate_expired_date = ' '.join(expired_date).strip()
        estate_seller_name = extract_with_css('div#LeftMainContent__productDetail_contactName div.right::text')
        estate_seller_address = extract_with_css('div#LeftMainContent__productDetail_contactAddress div.right::text')
        estate_seller_phone = extract_with_css('div#LeftMainContent__productDetail_contactPhone div.right::text')
        estate_seller_mobile = extract_with_css('div#LeftMainContent__productDetail_contactMobile div.right::text')
        estate_seller_email = extract_with_css('div#contactEmail div.right a::text')
        # start_date =dt.strptime(estate_date,"%d-%m-%Y")
        # end_date =dt.strptime(estate_expired_date,"%d-%m-%Y")
        estateItem = real_estateItem(estate_title= estate_title,estate_address=estate_address,estate_area=estate_area,estate_description=estate_description,estate_price=estate_price,estate_type=estate_type,estate_tag=estate_tag,estate_date=estate_date,estate_seller_name=estate_seller_name,estate_seller_address=estate_seller_address,estate_seller_phone=estate_seller_phone,estate_seller_mobile=estate_seller_mobile,estate_seller_email=estate_seller_email)
        # if start_date <= end_date:
        yield estateItem

from scrapy.crawler import CrawlerProcess
c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
})
c.crawl(RealEstateSpider)
c.start()