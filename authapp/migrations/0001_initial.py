# Generated by Django 2.2.17 on 2020-12-27 17:28

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postal_code', models.CharField(blank=True, max_length=6, null=True, verbose_name='индекс')),
                ('country', models.CharField(blank=True, max_length=30, null=True, verbose_name='страна')),
                ('region', models.CharField(blank=True, max_length=30, null=True, verbose_name='область')),
                ('district', models.CharField(blank=True, max_length=30, null=True, verbose_name='район')),
                ('microdistrict', models.CharField(blank=True, max_length=30, null=True, verbose_name='микрорайон')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='город')),
                ('street', models.CharField(blank=True, max_length=60, null=True, verbose_name='улица')),
                ('house', models.CharField(blank=True, max_length=6, null=True, verbose_name='дом')),
                ('apartment', models.CharField(blank=True, max_length=3, null=True, verbose_name='квартира')),
            ],
        ),
        migrations.CreateModel(
            name='Counteragent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_counteragent', models.CharField(choices=[('juridical_person', 'юридическое лицо'), ('physical_person', 'физическое лицо'), ('separate_subdivision', 'обособленное подразделение'), ('government_agency', 'государственный орган')], max_length=40, verbose_name='тип контрагента')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('surname', models.CharField(blank=True, max_length=40, null=True, verbose_name='отчество')),
                ('avatar', models.ImageField(blank=True, upload_to='users_avatars')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='день рождения')),
                ('access_right', models.SmallIntegerField(default=0, verbose_name='права доступа')),
                ('type_users', models.CharField(choices=[('natural_person', 'физическое лицо'), ('staff_member', 'штатный сотрудник'), ('freelancer', 'внештатный сотрудник')], max_length=40, verbose_name='тип пользователя')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='authapp.Address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
