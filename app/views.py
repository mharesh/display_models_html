from django.shortcuts import render
from app.models import *
# Create your views here.

def display_topic(request):
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSWO=Webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    QSAO=Accessrecord.objects.all()
    d={'QSAO':QSAO}
    return render(request,'display_accessrecord.html',d)