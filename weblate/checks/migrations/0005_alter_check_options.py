# Generated by Django 3.2 on 2021-05-12 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("checks", "0004_auto_20200516_1821"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="check",
            options={
                "verbose_name": "Quality check",
                "verbose_name_plural": "Quality checks",
            },
        ),
    ]