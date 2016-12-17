#!/usr/bin/env python
# encoding: utf-8


from django.db import models


class House(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    area = models.IntegerField()
    households = models.IntegerField()
    volume_rage = models.DecimalField()
    greening_rate = models.DecimalField()
