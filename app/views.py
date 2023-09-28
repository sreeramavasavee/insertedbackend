from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    t=input('enter topic name:')
    to=topic.objects.get_or_create(topic_name=t)[0]
    to.save()
    return HttpResponse('inserted successfully...')

def insert_webpage(request):
    t=input('enter topic name:')
    to=topic.objects.get_or_create(topic_name=t)[0]
    to.save()
    name=input('enter a name:')
    url=input('enter url:')
    no=webpage.objects.get_or_create(topic_name=to,name=name,url=url)[0]
    no.save()
    return HttpResponse('data inserted successfully..')

def insert_accessrecords(request):
    t=input('enter topic name:')
    to=topic.objects.get_or_create(topic_name=t)[0]
    to.save()
    name=input('enter a name:')
    url=input('enter url:')
    no=webpage.objects.get_or_create(topic_name=to,name=name,url=url)[0]
    no.save()
    date=input('enter date:')
    author=input('enter author:')
    aro=accessrecords.objects.get_or_create(name=no,date=date,author=author)[0]
    aro.save()
    return HttpResponse('inserted data to accessrcords successfully..')

