# Generated by Django 3.1.7 on 2021-04-02 12:05

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("metrics", "0006_auto_20210331_1047"),
    ]

    operations = [
        migrations.AlterField(
            model_name="metric",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
    ]