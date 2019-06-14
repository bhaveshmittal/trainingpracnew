import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","jobinfo.settings")
import django
django.setup()

from jobapp.models import *
from faker import Faker
from random import *
fake=Faker()

def phonenumbergen():
    d1=randint(7,9)
    num=''+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return num

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=("project manager","software engineer","sr. software analyst"))
        feligibility=fake.random_element(elements=("B.Tech","M.Tech","BBA"))
        faddress=fake.city()
        femail=fake.email()
        fphonenumber=phonenumbergen()
        jaipur_jobs=jaipurjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)
        gurgaon_jobs=gurgaonjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber=fphonenumber)

populate(25)
