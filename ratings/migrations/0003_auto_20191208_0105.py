# Generated by Django 2.2.7 on 2019-12-08 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0002_auto_20191207_2302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cookrating',
            old_name='item',
            new_name='cook',
        ),
        migrations.RenameField(
            model_name='customerrating',
            old_name='item',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='deliveryrating',
            old_name='item',
            new_name='delivery',
        ),
    ]
