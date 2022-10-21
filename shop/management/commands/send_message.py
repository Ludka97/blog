import asyncio

from django.conf import settings
from django.core.management.base import BaseCommand

# from game.bot import run_bot
from game.services import send_message


class Command(BaseCommand):
    help = "Run telegram bot"

    def handle(self, *args, **options):
        asyncio.run(send_message(chat_id=settings.CHAT_ID, text="Test notification"))
