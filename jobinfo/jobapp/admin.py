# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from jobapp.models import jaipurjobs,gurgaonjobs
# Register your models here.

class jaipurjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']

class gurgaonjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonenumber']


admin.site.register(jaipurjobs,jaipurjobsAdmin)
admin.site.register(gurgaonjobs,gurgaonjobsAdmin)
