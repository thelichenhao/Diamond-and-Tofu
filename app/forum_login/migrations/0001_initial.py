# Generated by Django 4.1.7 on 2023-05-06 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(default='Anonymous', max_length=100)),
                ('tofu_credit', models.IntegerField(default=0)),
                ('gender', models.CharField(default='I do not wish to provide this information', max_length=50)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('avatar', models.ImageField(blank=True, upload_to='avatars/')),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum_login.address')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
