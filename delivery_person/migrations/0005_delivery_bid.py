# Generated by Django 2.2.7 on 2019-12-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_person', '0004_auto_20191206_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='bid',
            field=models.FloatField(default=-1),
        ),
    ]
