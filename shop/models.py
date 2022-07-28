from django.conf import settings
from django.db import models

COLOR_CHOICES = (('red', 'Red color'), ('green', 'Green color'), ('white', 'White color'))

class Product(models.Model):
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=COLOR_CHOICES, blank=True, null=True)
    cost = models.IntegerField()


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="purchases", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    count = models.IntegerField()

# Create your models here.
