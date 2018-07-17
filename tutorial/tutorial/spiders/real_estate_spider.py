import scrapy
from ..items import real_estateItem
from scrapy.utils.markup import remove_tags
from scrapy_splash import SplashRequest
class RealEstateSpider(scrapy.Spider):
    name = "estate"
    
    def start_requests(self):
        yield SplashRequest(
            start_urls = 'https://batdongsan.com.vn/nha-dat-ban/p1',
            callback=self.parse,
        )
    

    def parse(self, response):
        # follow links to estate page
        for href in response.css('div.p-title h3 a::attr(href)'):
            yield response.follow(href, self.parse_estate)

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
        estate_seller_name = extract_with_css('div#LeftMainContent__productDetail_contactName div.right::text')
        estate_seller_address = extract_with_css('div#LeftMainContent__productDetail_contactAddress div.right::text')
        estate_seller_phone = extract_with_css('div#LeftMainContent__productDetail_contactPhone div.right::text')
        estate_seller_mobile = extract_with_css('div#LeftMainContent__productDetail_contactMobile div.right::text')
        estate_seller_email = extract_with_css('div#contactEmail div.right a::text')

        estateItem = real_estateItem(estate_title= estate_title,estate_address=estate_address,estate_area=estate_area,estate_description=estate_description,estate_price=estate_price,estate_type=estate_type,estate_tag=estate_tag,estate_seller_name=estate_seller_name,estate_seller_address=estate_seller_address,estate_seller_phone=estate_seller_phone,estate_seller_mobile=estate_seller_mobile,estate_seller_email=estate_seller_email)
        yield estateItem