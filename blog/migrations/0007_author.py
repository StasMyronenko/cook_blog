# Generated by Django 3.2.7 on 2021-10-07 15:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('about', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(upload_to='authors')),
            ],
        ),
    ]