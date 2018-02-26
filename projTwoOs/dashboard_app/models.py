# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from authApp.models import User
from django.db import models

# Create your models here.

class Glasses(models.Model):
    name = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='glasses')
