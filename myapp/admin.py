from django.contrib import admin
from django.contrib.admin.sites import site
from .models import Images
# Register your models here.

class ImagesAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']


admin.site.register(Images,ImagesAdmin)    