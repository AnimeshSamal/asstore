# Generated by Django 3.1.3 on 2021-01-12 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_mens_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mens',
            name='slug',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
