# Generated by Django 5.0.1 on 2024-02-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myntraData", "0009_product_catname"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="boughtproduct",
            name="product_id",
        ),
        migrations.AddField(
            model_name="boughtproduct",
            name="product",
            field=models.ManyToManyField(default="", to="myntraData.product"),
        ),
    ]
