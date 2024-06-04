# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class Article(Item):
    url = Field()
    date = Field()
    article_type = Field()
    title = Field()
    subtitle = Field()
    estimated_reading_time_minutes = Field()
    content = Field()
