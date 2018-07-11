import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'bmw'

    start_urls = ['https://bonbanh.com/oto/bmw/page,%s' % page for page in range(1,23)]

    def parse(self, response):
        # link den trang oto
        urls=response.css('li.car-item a::attr(href)').extract()
        for url in urls:
            url=response.urljoin(url)
            yield scrapy.Request(url=url,callback=self.parse_bmw)
        # # link den trang tiep theo
        # next_page_url=response.css('div.navpage span:nth-child(7)::attr(url)').extract_first()
        # if next_page_url:
        #     next_page_url=response.urljoin(next_page_url)
        #     yield scrapy.Request(url=next_page_url,callback=self.parse)

    def parse_bmw(self, response):
        yield {
            'name':response.css('i[itemprop="name"]::text').extract_first(),
        }