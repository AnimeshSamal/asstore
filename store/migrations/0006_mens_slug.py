# Generated by Django 3.1.3 on 2021-01-12 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_mens'),
    ]

    operations = [
        migrations.AddField(
            model_name='mens',
            name='slug',
            field=models.ImageField(null=True, upload_to='uploads/mens/'),
        ),
    ]
