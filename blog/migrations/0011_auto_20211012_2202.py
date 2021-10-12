# Generated by Django 3.2.7 on 2021-10-12 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_create_as'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='create_as',
        ),
        migrations.AddField(
            model_name='comment',
            name='create_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
