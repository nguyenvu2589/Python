from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField
from decimal import Decimal


class Document(models.Model):
    name = models.CharField(max_length=128)
    numEntry = models.IntegerField(max_length=10, default= 0)
    document = models.FileField(upload_to = 'uploads/photo/%Y/%m/')
    time = models.DateTimeField(auto_now_add = True)




