import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

from main.scraper.scraper.items import ScraperItem


class PropertiesSpider(CrawlSpider):  # scrapy.Spider
    name = "properties"
    allowed_domains = ['https://www.goal.com']
    start_urls = [
        'https://www.goal.com/en-my/live-scores'
    ]

    # rules= (
    #     Rule(LinkExtractor(allow =()))
    # )

    def parse_property(self, response):
        property_loader = ItemLoader(item=ScraperItem(), response=response)
        property_loader.default_output_processor = TakeFirst()

        property_loader.add_css(
            "home_team", "span#team-home_team-name::text"
        )
        property_loader.add_css(
            "home_goals", "span#team-home_goals::text"
        )
        property_loader.add_css(
            "away_team", "span#team-away_away-team::text"
        )
        property_loader.add_css(
            "away_goals", "span#team-away_goals::text"
        )

        yield property_loader.load_item()

#     def parse(self, response):
#         # # page = response.url('/live-scores')
#         # filename = 'posts-%s.html'
#         # with open(filename, 'wb') as f:
#         #     f.write(response.body)  # copy the html file locally
#
#         for post in response.css('div.match-data'):
#             yield{
#                 'home_team': post.css('div.team-home span.team-name::text').getall()
# ,
#                 'home_score': post.css('div.team-home span.goals::text').getall()
# ,
#                 'away_team': post.css('div.team-away span.team-name::text').getall()
# ,
#                 'away_score': post.css('div.team-away span.goals::text').getall()
# ,
#             }
#
