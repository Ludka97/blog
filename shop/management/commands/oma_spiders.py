from django.core.management.base import BaseCommand
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher
from scrapy.utils.project import get_project_settings

from shop.models import Product
from shop.service import run_oma_spider
from shop.spiders import OmaSpider


class Command(BaseCommand):
    help = "Crawl OMA catalog"

    def handle(self, *args, **options):
        dry_run = options.get("dry_run", False)
        #run_oma_spider.delay(dry_run)
        run_oma_spider(dry_run)

