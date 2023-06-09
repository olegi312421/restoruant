# Generated by Django 4.1.7 on 2023-03-02 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('phone', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Erros', regex='\\+?3?8?0\\d{2}[- ]?(\\d[ -]?){7}$')])),
                ('persons', models.SmallIntegerField()),
                ('message', models.TextField(blank=True, max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_processed', models.DateField(auto_now=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]
