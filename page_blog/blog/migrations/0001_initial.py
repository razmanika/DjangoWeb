# Generated by Django 2.2.1 on 2019-06-11 07:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comm_author', models.CharField(blank=True, max_length=50)),
                ('publish_time', models.DateTimeField(verbose_name='Date Published')),
                ('content', models.TextField(default=django.utils.timezone.now)),
                ('on_post', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(blank=True, max_length=50)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('publish_time', models.DateTimeField(verbose_name='Date Published')),
                ('content', models.TextField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('pswd', models.CharField(blank=True, max_length=70)),
            ],
        ),
    ]
