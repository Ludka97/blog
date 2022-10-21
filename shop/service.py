from django.core.management.base import BaseCommand
from django.db.models import F, Sum

# from django_rq import job
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from shop.models import Product
from shop.spiders import OmaSpider


# @job
def run_oma_spider(dry_run: bool = False):
    if dry_run:
        Product.objects.all().delete()

    def crawler_results(signal, sender, item, response, spider):
        Product.objects.update_or_create(external_id=item["external_id"], defaults=item)

    dispatcher.connect(crawler_results, signal=signals.item_scraped)

    process = CrawlerProcess(get_project_settings())
    process.crawl(OmaSpider)
    process.start()


def get_popular_products():
    queryset = Product.objects.annotate(sold=Sum(F("cost") * F("purchases__count")))
    return queryset.order_by("-sold")
