# Generated by Django 4.2 on 2023-04-27 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='email')),
                ('first_name', models.CharField(max_length=150, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=150, verbose_name='last_name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='is_superuser')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation_date')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'ordering': ('-creation_date',),
            },
        ),
    ]
