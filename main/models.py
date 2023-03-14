import os.path
from django.core.validators import MaxValueValidator, MinValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django import forms
from django.core.validators import RegexValidator

import uuid

class Services(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)
    about = models.CharField(max_length=255)

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position',)

class Special_Dishes(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)
    ingredients = models.CharField(max_length=255)
    price = models.DecimalField(max_length=6, decimal_places=2, max_digits=1000)
    photo = models.ImageField(upload_to='dish/%Y-%m-%d', blank=True)
    discount = models.DecimalField(max_length=3, decimal_places=2, max_digits=1000)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ('position',)

    def get_discounted_price(self):
        return round(self.price * (1 - self.discount / 100), 2)

class Menu(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)
    desc = models.CharField(max_length=255, blank=True)
    ingredients = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recommended = models.BooleanField(default=False)
    price = models.DecimalField(max_length=6, decimal_places=2, max_digits=1000)
    photo = models.ImageField(upload_to='dish/%Y-%m-%d', blank=True)
    is_special = models.BooleanField(default=False, blank=True)

    def clean(self):
        if self.is_special and not self.desc and not self.photo:
            raise ValidationError('is_special is required when desc and photo  is True.')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('category', 'position')

class Podeia(models.Model):
    MONTH_CHOICES = (
        ('01', _('Січень')),
        ('02', _('Лютий')),
        ('03', _('Березень')),
        ('04', _('Квітень')),
        ('05', _('Травень')),
        ('06', _('Червень')),
        ('07', _('Липень')),
        ('08', _('Серпень')),
        ('09', _('Вересень')),
        ('10', _('Жовтень')),
        ('11', _('Листопад')),
        ('12', _('Грудень')),
    )
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    year = models.IntegerField(validators=[MinValueValidator(2023), MaxValueValidator(2024)])
    month = models.CharField(max_length=2, choices=MONTH_CHOICES)
    day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)])
    hour = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(23)])
    minute = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(59)])
    is_visible = models.BooleanField(default=True)
    desc = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='dish/%Y-%m-%d', blank=True)

    def get_month_display(self):
        return dict(self.MONTH_CHOICES)[self.month]

class Gallery(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='dish/%Y-%m-%d', blank=True)

    def __str__(self):
        return f'{self.title}'


class Reservation(models.Model):
    phone_validator = RegexValidator(regex=r'\+?3?8?0\d{2}[- ]?(\d[ -]?){7}$', message='Errors')

    name = models.CharField(max_length=50, db_index=True)
    phone = models.CharField(max_length=20, validators=[phone_validator])
    number_of_people = models.SmallIntegerField()
    message = models.TextField(max_length=250, blank=True)

    date_and_time = models.DateField()
    date_processed = models.DateField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    class Meta():
        ordering = ('-date_and_time',)

    def __str__(self):
        return f"{self.name}: {self.phone}"
