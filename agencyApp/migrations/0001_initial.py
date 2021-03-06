# Generated by Django 3.2.7 on 2021-10-08 15:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Country')),
                ('birthDay', models.DateField(blank=True, null=True, verbose_name='Birth Day')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('isActive', models.BooleanField(default=True)),
                ('discount', models.SmallIntegerField(default=0)),
                ('country', models.CharField(max_length=50)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('modifiedAt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('buyerID', models.IntegerField(default=1)),
                ('buyerCard', models.BigIntegerField(default=1111111111111111)),
                ('buyerCardName', models.CharField(max_length=50)),
                ('buyerCardDueDate', models.DateField()),
                ('buyerCardCVV', models.IntegerField(default=111)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('pack', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agencyApp.pack')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
