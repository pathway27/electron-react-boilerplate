"""ddd"""
# -*- coding: utf-8 -*-

import scrapy


class PS5Spider(scrapy.Spider):

    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_PlayStation_5_games',
        'https://en.wikipedia.org/wiki/List_of_handheld_game_consoles'
    ]
    wikipedia_table_css = '.wikitable'

    def parse(self, response):
        for wiki_table in response.css(self.wikipedia_table_css):
            table_headers = {}

            for platform_pre in wiki_table.css('tr'):
                # click link to platform
                # scrapy.Request(next_page, callback=self.parse)
                # infobox
                platform_infobox = 'asa'
                platform_info = {}

                for item in platform_infobox:
                    platform_info[item.css('td')] = platform_info.css('tr').extract_first()

                yield platform_info
