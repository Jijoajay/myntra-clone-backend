# Generated by Django 5.0.1 on 2024-02-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myntraData", "0012_alter_product_thumbimg"),
    ]

    operations = [
        migrations.CreateModel(
            name="BrandCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img", models.URLField()),
                ("brandName", models.CharField(max_length=50)),
                ("offer", models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name="product",
            name="clothingType",
            field=models.CharField(
                choices=[
                    ("Infant", "Infant"),
                    ("Topwear", "Topwear"),
                    ("Makeup", "Makeup"),
                    ("Skincare", "Skincare"),
                    ("Haircare", "Haircare"),
                    ("FootWear", "FootWear"),
                    ("Fragnance", "Fragnance"),
                    ("Sports & Active Wear", "Sports & Active Wear"),
                    ("Sportswear", "Sportswear"),
                    ("Sportswear", "Sportswear"),
                    ("bottomWear", "bottomWear"),
                    ("Indianwear", "Indianwear"),
                    ("Toys&Games", "Toys&Games"),
                    ("Boysclothing", "Boysclothing"),
                    ("Girlsclothing", "Girlsclothing"),
                    ("Men's Grooming", "Men's Grooming"),
                    ("Sleep&Innerwear", "Sleep&Innerwear"),
                    ("Kids Accessories", "Kids Accessories"),
                    ("Fashion Accesscories", "Fashion Accesscories"),
                ],
                max_length=20,
            ),
        ),
    ]
