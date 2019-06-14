# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from jobapp.models import *


def jaipurjobsview(request):
    jaipur_list=jaipurjobs.objects.all()
    print(jaipur_list)
    print("------------------")
    print(type(jaipur_list))
    mydict={'jaipur_list' : jaipur_list}
    return render(request,'jobapp/jaipurjobinfo.html',context=mydict)
