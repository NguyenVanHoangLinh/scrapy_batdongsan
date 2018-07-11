import scrapy
class QuotesSpider(scrapy.Spider):
    name = "dantri"
    start_urls = [
        'http://dantri.com.vn/tam-long-nhan-ai.htm',
    ]
    def parse(self, response):
        for article in response.css('div.eplcheck'):
            yield {
                'title': article.css('div.mr1 a.fon6::text').extract_first(),
            }
        next_page = response.css('div.fr a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
           
        