# Generated by Django 4.0 on 2022-12-22 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0015_news_body_en_news_body_ru_news_body_uz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='body_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='body_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='body_uz',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_ru',
        ),
        migrations.RemoveField(
            model_name='news',
            name='title_uz',
        ),
    ]
