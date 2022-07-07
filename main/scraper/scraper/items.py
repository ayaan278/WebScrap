from scrapy_djangoitem import DjangoItem
from main.properties.models import Scores


class ScraperItem(DjangoItem):
    django_model = Scores

    SPIDER_MODULES = ['scraper.scraper.spiders']
    NEWSPIDER_MODULE = 'scraper.scraper.spiders'

    # Obey robots.txt rules
    ROBOTSTXT_OBEY = True

    # update the pipelines to this
    ITEM_PIPELINES = {
        'scraper.scraper.pipelines.PropertyStatusPipeline': 100,
        'scraper.scraper.pipelines.PropertyPricePipeline': 200,
        'scraper.scraper.pipelines.ConvertNumPipeline': 300,
        'scraper.scraper.pipelines.ScraperPipeline': 400,
    }