# -*- coding: utf-8 -*-
import scrapy
import datetime

from scraper.models.wikipedia_table import WikipediaTable

class CalendarSpider(scrapy.Spider):
    name = 'calendar'

    tables_xpath = "//*[@class='mw-headline'][@id='Game_releases']/../following-sibling::table"
    start_year = 2011
    final_year = datetime.datetime.now().year + 1

    @property
    def start_urls(self):
        return [
            "https://en.wikipedia.org/wiki/{}_in_video_gaming".format(x)
            for x in range(self.start_year, self.final_year)
        ]

    def parse(self, response):
        print(self.start_urls)
        platforms, q1, q2, q3, q4, *others = response.xpath(self.tables_xpath)

        for quarter_table in [q1, q2, q3, q4]:
            WikipediaTable(quarter_table).run2()
