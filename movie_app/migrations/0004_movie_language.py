# Generated by Django 5.0.1 on 2024-01-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0003_alter_movie_video"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="language",
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
