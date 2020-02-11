# Generated by Django 3.0.3 on 2020-02-11 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='bottomsize',
            new_name='bottom_size',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='shoesize',
            new_name='shoe_size',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='topsize',
            new_name='top_size',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='user',
            new_name='user_id',
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]