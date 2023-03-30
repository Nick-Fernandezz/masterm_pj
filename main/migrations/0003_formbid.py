# Generated by Django 4.1.7 on 2023-03-04 13:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_moderators_remove_socialclub_media_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormBid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(editable=False, max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message='Номер не соответствует формату. +79999999999', regex='^\\+?7?\\d{9, 15}')])),
                ('status', models.BooleanField(default=False, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'заявку',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
