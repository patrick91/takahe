# Generated by Django 4.1.7 on 2023-03-11 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activities", "0012_in_reply_to_index"),
        ("users", "0015_bookmark"),
    ]

    operations = [
        migrations.CreateModel(
            name="HashtagFollow",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "hashtag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="followers",
                        to="activities.hashtag",
                    ),
                ),
                (
                    "identity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hashtag_follows",
                        to="users.identity",
                    ),
                ),
            ],
            options={
                "unique_together": {("identity", "hashtag")},
            },
        ),
    ]