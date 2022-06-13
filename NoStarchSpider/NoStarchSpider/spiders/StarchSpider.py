import scrapy


class StarchspiderSpider(scrapy.Spider):
    name = 'StarchSpider'
    allowed_domains = ['nostarch.com']
    start_urls = ['http://nostarch.com/catalog/python']

    def parse(self, response):
        books = response.xpath("//div[@class='col-xs-6 col-sm-6 col-md-6 col-lg-6 with-padding-bottom nostrach-views-row']/div[2]")
        for book in books:
            yield{
                'book_name': book.xpath(".//div[@class='product-title']/a/text()").get(),
                'book_info': book.xpath(".//div[2]/text()").get(),
                'book_author': book.xpath(".//div[3]/text()").get(),
                'book_price': book.xpath(".//span[@class='uc-price']/text()").get(),
                'published_on': book.xpath("normalize-space(.//div[@class='product-author']/following-sibling::text())").get().strip(),
            }
