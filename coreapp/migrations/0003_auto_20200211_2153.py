# Generated by Django 3.0.3 on 2020-02-11 21:53

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0002_auto_20200211_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]