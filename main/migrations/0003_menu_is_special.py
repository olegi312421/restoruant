# Generated by Django 4.1.6 on 2023-02-20 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_category_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
    ]