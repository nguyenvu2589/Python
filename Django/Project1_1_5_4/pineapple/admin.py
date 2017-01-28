from django.contrib import admin
from pineapple.models import Category, Page
from django.db import models
from django.contrib.auth.models import User


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'views', 'price','image')

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank = True)

    def __unicode__(self):
        return self.user.username


admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Page, PageAdmin)