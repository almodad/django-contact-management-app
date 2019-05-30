# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
