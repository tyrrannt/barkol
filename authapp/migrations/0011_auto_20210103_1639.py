# Generated by Django 2.2.17 on 2021-01-03 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_auto_20210103_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='city_id',
            field=models.CharField(blank=True, max_length=30, verbose_name=''),
        ),
    ]