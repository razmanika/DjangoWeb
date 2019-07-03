# Generated by Django 2.2.1 on 2019-06-11 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190611_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Comm_author',
        ),
        migrations.AddField(
            model_name='comment',
            name='comm_author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
            preserve_default=False,
        ),
    ]