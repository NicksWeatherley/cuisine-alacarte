# Generated by Django 2.2.7 on 2019-11-25 02:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cook', '0003_auto_20191125_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='warnings',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(3)]),
        ),
    ]
