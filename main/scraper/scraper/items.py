from scrapy_djangoitem import DjangoItem
from properties.models import Property


class ScraperItem(DjangoItem):
    django_model = Property
