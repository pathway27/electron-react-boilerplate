# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class NeoSeekerGame(scrapy.Item):
    name = scrapy.Field()
    minipic = scrapy.Field()
    date = scrapy.Field()
    platform = scrapy.Field()
    genre = scrapy.Field()

class Game(scrapy.Item):
    name = scrapy.Field()
    release_date = scrapy.Field()
    platforms = scrapy.Field()
    publishers = scrapy.Field()
    genres = scrapy.Field()


class Platform(scrapy.Item):
    name = scrapy.Field()
    release_date = scrapy.Field()

