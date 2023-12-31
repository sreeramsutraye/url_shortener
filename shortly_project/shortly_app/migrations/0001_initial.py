# Generated by Django 4.2.3 on 2023-07-20 12:21

from django.db import migrations, models
import shortly_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortURL",
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
                ("original_url", models.URLField()),
                (
                    "short_url",
                    models.CharField(
                        default=shortly_app.models.generate_random_short_url,
                        max_length=6,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
