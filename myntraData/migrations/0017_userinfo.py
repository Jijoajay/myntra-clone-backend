# Generated by Django 5.0.1 on 2024-02-25 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myntraData", "0016_user_pin_code"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
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
                ("full_name", models.CharField(max_length=30)),
                ("email", models.CharField(max_length=30)),
                ("gender", models.CharField(max_length=10)),
                ("birthday", models.CharField(max_length=10)),
                ("alternate_mobile_number", models.IntegerField()),
                ("hint", models.CharField(max_length=20)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_info",
                        to="myntraData.user",
                    ),
                ),
            ],
        ),
    ]
