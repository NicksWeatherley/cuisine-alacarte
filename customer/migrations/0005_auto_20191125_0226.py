# Generated by Django 2.2.7 on 2019-11-25 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20191125_0210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='rating',
            new_name='restaurant_ratings',
        ),
    ]
