# Generated by Django 2.2.17 on 2021-01-04 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0020_auto_20210104_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='access_right',
            field=models.ManyToManyField(default=0, to='libapp.AccessLevel', verbose_name='права доступа'),
        ),
    ]
