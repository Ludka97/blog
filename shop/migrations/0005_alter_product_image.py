# Generated by Django 4.0.6 on 2022-08-19 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0004_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
    ]
