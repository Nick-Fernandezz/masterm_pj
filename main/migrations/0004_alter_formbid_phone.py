# Generated by Django 4.1.7 on 2023-03-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_formbid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formbid',
            name='phone',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]
