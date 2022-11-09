# Generated by Django 4.1.3 on 2022-11-09 06:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'ims_app_users',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'ims_categories',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('particular', models.TextField(max_length=500)),
                ('ledger_folio', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField()),
                ('prince', models.FloatField()),
                ('total', models.FloatField()),
                ('entry_date', models.DateTimeField(default=datetime.datetime(2022, 11, 9, 12, 1, 17, 341633))),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_mini.category')),
            ],
            options={
                'db_table': 'ims_items',
            },
        ),
    ]
