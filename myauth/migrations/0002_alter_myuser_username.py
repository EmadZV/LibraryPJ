# Generated by Django 4.1 on 2022-09-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='username',
            field=models.CharField(blank=True, default=None, max_length=20, null=True, unique=True),
        ),
    ]