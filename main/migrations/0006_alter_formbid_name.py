# Generated by Django 4.1.7 on 2023-03-04 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_formbid_name_alter_formbid_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formbid',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]