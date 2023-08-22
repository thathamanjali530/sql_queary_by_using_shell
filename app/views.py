from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.

def Insert_Topic(request):
    tn=input('enter topic name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('data inserted')


def Insert_Webpage(request):
    tn=input('enter topic name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name : ')
    u=input('enter url : ')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    return HttpResponse('DATA INSERTED')


def Insert_AccessRecord(request):
    tn=input('enter topic name : ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('enter name : ')
    u=input('enter url : ')
    wo=Webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    d=input('enter date : ')
    a=input('enter author : ')
    e=input('enter email : ')
    Ao=AccessRecord.objects.get_or_create(name=wo,date=d,author=a,email=e)[0]
    Ao.save()
    return HttpResponse('DATA INSERTED')