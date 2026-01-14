from django.shortcuts import render

from django.http import HttpResponse

from app.models import *

# Create your views here.

def insert_Topic(request):
    tn = input('Enter topic name:')
    TTO= Topic.objects.get_or_create(topic_name = tn)
    if TTO[1]:
        return HttpResponse('New topic is created')
    else:
        return HttpResponse('Topic is already present')

def insert_webpage(request):
    print('Existing topic')
    for to in Topic.objects.all():
        print(to.topic_name)
    tn = input('enter the name of topic:')
    LTO = Topic.objects.filter(topic_name = tn)
    if LTO:
        STO = LTO[0]
        na = input('enter the name:')
        ur = input('enter the url:')
        TWO = Webpage.objects.get_or_create(topic =STO, name=na, url =ur)
        if TWO[1]:
            return HttpResponse('New webpage is created')
        else:
            return HttpResponse('Webpage is already present')
    else:
        return HttpResponse('Topic is not present')
    
def insert_Accessrecord(request):
    print('Existing Web pages')
    for wp in Webpage.objects.all():
        print(wp.name)
    wn = input('Enter the webpage name')
    LWO = Webpage.objects.filter(name = wn)
    if LWO:
        SWO =LWO[0]    
        at = input('Enter the author name :')
        da = input('Enter the date:')
        TWO = AccessRecord.objects.get_or_create(name = SWO,Author = at ,date = da,)
        if TWO[1]:
            return HttpResponse('New accessrecord is created')
        else:
            return HttpResponse('Accessrecord is already present')
        
    else:
        return HttpResponse('Webpage is not present')
    
    