# Generated by Django 4.1 on 2022-09-08 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0001_initial'),
        ('mycontent', '0002_alter_book_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='myshop.price'),
        ),
    ]
