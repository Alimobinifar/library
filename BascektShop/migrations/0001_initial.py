# Generated by Django 4.0.1 on 2022-01-26 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('book', '0011_alter_book_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('count', models.IntegerField()),
                ('status', models.CharField(choices=[('ok', 'خرید نهایی شده '), ('pending', 'در انتظار پرداخت'), ('cancelled', 'انصراف از خرید')], default='pending', max_length=15)),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='BascektShop.finalbasket')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]