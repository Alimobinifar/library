# Generated by Django 4.0.1 on 2022-01-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publisher',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]