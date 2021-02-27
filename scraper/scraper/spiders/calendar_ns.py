# -*- coding: utf-8 -*-
import scrapy

from scrapy.loader import ItemLoader

from scraper.items import NeoSeekerGame

# Neoskeeker Calendar Spider
class CalendarNsSpider(scrapy.Spider):
    name = 'calendar_ns'
    start_urls = ['http://www.neoseeker.com/Games/releases/']
    game_row_css = 'table.releases_list tr'

    def parse(self, response):
        for game in response.css(self.game_row_css):
            l = ItemLoader(item=NeoSeekerGame())

            # link to game also there
            l.add_value('name', game.css('td.releases_item_name a::text, a strong::text').extract_first())
            l.add_value('minipic', game.css('td.releases_item_minipic img::attr(src)').extract_first())
            l.add_value('date', game.css('td.releases_item_date::text').extract_first())
            l.add_value('platform', game.css('td.releases_item_platforms a::text').extract_first())
            l.add_value('genre', game.css('td.releases_item_genre a::text').extract_first())
            yield l.load_item()
