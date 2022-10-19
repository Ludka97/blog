from django.conf import settings
from django.db import models


class Address(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="address",
        blank=True,
        null=True,
    )

    city = models.CharField(max_length=200)
    address = models.CharField(max_length=200)


# Create your models here.
