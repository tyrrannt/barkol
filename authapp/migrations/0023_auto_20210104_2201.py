# Generated by Django 2.2.17 on 2021-01-04 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0022_auto_20210104_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='corp_phone',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corp', to='authapp.PhoneNumber', verbose_name='корпоративный номер'),
        ),
        migrations.AlterField(
            model_name='person',
            name='phone',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cell', to='authapp.PhoneNumber', verbose_name='номер телефона'),
        ),
    ]
