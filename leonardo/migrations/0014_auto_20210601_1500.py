# Generated by Django 2.2.2 on 2021-06-01 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leonardo', '0013_auto_20210201_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='nyhet',
            name='external_link',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='nyhet',
            name='link_text',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]