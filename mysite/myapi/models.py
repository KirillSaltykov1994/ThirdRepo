# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Staff(models.Model):

    id = models.IntegerField(primary_key=True)
    uid = models.CharField(max_length=100)
    strain = models.CharField(max_length=100)
    cannabinoid_abbreviation = models.CharField(max_length=100)
    cannabinoid = models.CharField(max_length=100)
    terpene = models.CharField(max_length=100)
    medical_use = models.CharField(max_length=100)
    health_benefit = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    buzzword = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.uid
