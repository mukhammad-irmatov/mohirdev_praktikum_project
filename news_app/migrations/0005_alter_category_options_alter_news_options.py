# Generated by Django 4.0 on 2022-12-15 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0004_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-publish_time'], 'verbose_name_plural': 'News'},
        ),
    ]
