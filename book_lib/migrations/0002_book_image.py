# Generated by Django 5.0.1 on 2024-02-05 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_lib', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/%y/%m/%d'),
        ),
    ]
