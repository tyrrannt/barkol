# Generated by Django 2.2.17 on 2021-01-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('authapp', '0015_auto_20210103_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather',
            name='weather_date',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
