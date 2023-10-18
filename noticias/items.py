import scrapy


class NoticiasItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    text = scrapy.Field()
    link = scrapy.Field()