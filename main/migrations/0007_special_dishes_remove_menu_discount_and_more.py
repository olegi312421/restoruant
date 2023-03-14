# Generated by Django 4.1.7 on 2023-02-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_menu_is_firm_alter_menu_is_special'),
    ]

    operations = [
        migrations.CreateModel(
            name='Special_Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.SmallIntegerField(unique=True)),
                ('ingredients', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=1000, max_length=6)),
                ('photo', models.ImageField(blank=True, upload_to='dish/%Y-%m-%d')),
                ('discount', models.DecimalField(decimal_places=2, max_digits=1000, max_length=3)),
            ],
        ),
        migrations.RemoveField(
            model_name='menu',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='is_firm',
        ),
    ]