# Generated by Django 5.0.1 on 2024-01-07 12:06

import autoslug.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie_app", "0006_genre_is_active_movie_is_active"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comments",
            name="comment",
        ),
        migrations.AddField(
            model_name="genre",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=1, editable=False, populate_from="title", unique=True
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="movie",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=1, editable=False, populate_from="title", unique=True
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=1, editable=False, populate_from="get_full_name", unique=True
            ),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name="comments",
            name="movie",
        ),
        migrations.AddField(
            model_name="comments",
            name="movie",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="movie_app.movie",
            ),
            preserve_default=False,
        ),
    ]
