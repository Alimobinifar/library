# Generated by Django 4.0.1 on 2022-01-25 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_rename_category_category_title_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publishe', to='book.publisher'),
        ),
    ]
