# Generated by Django 2.2.17 on 2021-01-04 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0018_auto_20210104_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='works',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='authapp.Work', verbose_name='занятость'),
        ),
    ]
