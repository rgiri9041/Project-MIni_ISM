# Generated by Django 4.1.3 on 2022-11-17 07:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_mini', '0002_item_rename_first_name_appuser_fist_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='entry_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 13, 41, 50, 842963), null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='update_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 17, 13, 41, 50, 842963), null=True),
        ),
    ]
