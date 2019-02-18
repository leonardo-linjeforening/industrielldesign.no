# Generated by Django 2.0.1 on 2018-05-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_remove_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]