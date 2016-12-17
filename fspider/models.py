from __future__ import unicode_literals

from django.db import models


# Create your models here.
class House(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='N/A')
    area = models.IntegerField(default=0)
    households = models.IntegerField(default=0)
    volume_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    greening_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    href = models.CharField(max_length=200, default='')


class Villa(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='N/A')
    area = models.IntegerField(default=0)
    households = models.IntegerField(default=0)
    volume_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    greening_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    href = models.CharField(max_length=200, default='')


class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='N/A')
    category = models.CharField(max_length=100, default='N/A')
    area = models.IntegerField(default=0)
    parking = models.CharField(max_length=100, default='N/A')
    href = models.CharField(max_length=200, default='')


class Office(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default='N/A')
    category = models.CharField(max_length=100, default='N/A')
    area = models.IntegerField(default=0)
    parking = models.CharField(max_length=100, default='N/A')
    href = models.CharField(max_length=200, default='')
