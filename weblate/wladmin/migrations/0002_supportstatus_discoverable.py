# Generated by Django 3.1.7 on 2021-03-12 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wladmin", "0001_squashed_0008_auto_20191011_0816"),
    ]

    operations = [
        migrations.AddField(
            model_name="supportstatus",
            name="discoverable",
            field=models.BooleanField(default=False),
        ),
    ]
