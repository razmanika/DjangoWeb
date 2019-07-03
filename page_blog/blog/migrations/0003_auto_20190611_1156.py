# Generated by Django 2.2.1 on 2019-06-11 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190611_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Comm_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='on_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
