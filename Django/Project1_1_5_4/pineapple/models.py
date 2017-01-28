from django.db import models
from django.contrib import admin
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from easy_thumbnails.fields import ThumbnailerImageField
from decimal import Decimal

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    view = models.IntegerField(max_length=10, default= 0)
    likes= models.IntegerField(max_length =10, default= 0)
    slug = models.SlugField(default='')

    def save(self, *args, ** kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    views = models.IntegerField(max_length=10, default= 0)
    price = models.DecimalField(max_digits=20,decimal_places=4,null= True)
    feature = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/images/', default ='static/images/coming.jpeg')
    des = models.CharField(max_length=9999)
    slugP = models.SlugField(default='')

    def save(self, *args, ** kwargs):
        self.slugP = slugify(self.title)
        super(Page, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

class Document(models.Model):
    name = models.CharField(max_length=128)
    numEntry = models.IntegerField(max_length=10, default= 0)
    document = models.FileField(upload_to = 'uploads/photo/%Y/%m/')
    time = models.DateTimeField(auto_now_add = True)

# update FileField that only allow .csv file - match ="*.csv"


