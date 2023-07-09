# Generated by Django 4.2.1 on 2023-06-19 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("basic_app", "0003_enquery"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("blogdate", models.DateField(auto_created=True, max_length=10)),
                ("Title", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=20)),
                ("image", models.ImageField(upload_to="")),
                ("description", models.TextField(max_length=200)),
            ],
        ),
    ]