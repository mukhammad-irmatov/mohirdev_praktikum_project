# Generated by Django 4.0 on 2022-12-21 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0011_remove_news_view_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
