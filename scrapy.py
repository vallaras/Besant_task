import scrapy
class HandlerItem(scrapy.Item):
    link = scrapy.Field()
    link2 = scrapy.Field()
    domainlink = scrapy.Field()
    twitterlink = scrapy.Field()
    twitterlink2 = scrapy.Field()
    twitterlinku = scrapy.Field()
    handles = scrapy.Field()
    pass