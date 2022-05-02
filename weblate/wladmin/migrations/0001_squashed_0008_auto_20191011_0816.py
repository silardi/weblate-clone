# Generated by Django 3.0.5 on 2020-04-16 11:24

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

import weblate.utils.backup


class Migration(migrations.Migration):

    replaces = [
        ("wladmin", "0001_squashed_0003_auto_20180215_1127"),
        ("wladmin", "0002_auto_20181127_2116"),
        ("wladmin", "0003_auto_20190516_1250"),
        ("wladmin", "0004_supportstatus"),
        ("wladmin", "0005_auto_20190926_1332"),
        ("wladmin", "0006_auto_20190926_1218"),
        ("wladmin", "0007_auto_20190926_1406"),
        ("wladmin", "0008_auto_20191011_0816"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ConfigurationError",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
                ("message", models.TextField()),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                ("ignored", models.BooleanField(db_index=True, default=False)),
            ],
            options={"index_together": {("ignored", "timestamp")}},
        ),
        migrations.CreateModel(
            name="BackupService",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "repository",
                    models.CharField(
                        default="",
                        max_length=500,
                        verbose_name="Backup repository URL",
                        help_text="Use /path/to/repo for local backups or user@host:/path/to/repo for remote SSH backups.",
                    ),
                ),
                ("enabled", models.BooleanField(default=True)),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                ("paperkey", models.TextField()),
                (
                    "passphrase",
                    models.CharField(
                        default=weblate.utils.backup.make_password, max_length=100
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SupportStatus",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("secret", models.CharField(max_length=400)),
                ("expiry", models.DateTimeField(db_index=True, null=True)),
                ("in_limits", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="BackupLog",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "event",
                    models.CharField(
                        choices=[
                            ("backup", "Backup performed"),
                            ("error", "Backup failed"),
                            ("prune", "Deleted the oldest backups"),
                            ("init", "Repository initialization"),
                        ],
                        max_length=100,
                    ),
                ),
                ("log", models.TextField()),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wladmin.BackupService",
                    ),
                ),
            ],
        ),
    ]
