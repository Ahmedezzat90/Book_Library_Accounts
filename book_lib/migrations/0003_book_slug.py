# Generated by Django 4.2.4 on 2024-02-06 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_lib', '0002_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
