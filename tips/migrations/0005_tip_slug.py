# Generated by Django 2.2.2 on 2019-06-23 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0004_auto_20190623_1201'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='slug',
            field=models.SlugField(default='Heisann'),
            preserve_default=False,
        ),
    ]