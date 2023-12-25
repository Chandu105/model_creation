from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q

# Create your views here.
def display_topics(request):
    QLTO=Topic.objects.all().order_by('topic_name')
    QLTO=Topic.objects.all().order_by('-topic_name')
    QLTO=Topic.objects.all().order_by(Length('topic_name'))
    QLTO=Topic.objects.all().order_by(Length('topic_name').desc())
    QLTO=Topic.objects.exclude(topic_name='cricket')
    

    d={'topics':QLTO}
    return render(request,'display_topics.html',d)
    

def display_webpage(request):
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(name__startswith='m')
    QLWO=Webpage.objects.filter(name__endswith='l')
    QLWO=Webpage.objects.filter(name__contains='a')
    QLWO=Webpage.objects.filter(name__in=('rahul','ronaldo'))
    QLWO=Webpage.objects.all()
    QLWO=Webpage.objects.filter(topic_name='cricket',url__endswith='in')
    QLWO=Webpage.objects.filter(Q(topic_name='cricket') | Q(url__endswith='in'))
   
    


    d={'QLWO':QLWO}
    
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    QLAO=AccessRecord.objects.filter(date__year='2022')
    QLAO=AccessRecord.objects.filter(date__month='12')
    QLAO=AccessRecord.objects.filter(date__day='14')
    QLAO=AccessRecord.objects.filter(date__gt='2023-12-13')
    QLAO=AccessRecord.objects.filter(date__lt='2023-12-13')
    QLAO=AccessRecord.objects.filter(date__gte='2023-12-15')
    QLAO=AccessRecord.objects.filter(date__lte='2023-12-7')



    
    
    
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)

def insert_topics(request):
    tn=input('enter here: ')
    NTO=Topic.objects.get_or_create(topic_name=tn)[0]
    NTO.save()
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topics.html',d)

def insert_webpage(request):
    tn=input('enter tn: ')
    n=input('enter name: ')
    u=input('enter url: ')
    TO=Topic.objects.get(topic_name=tn)

    NWO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    NWO.save()
    QLWO=Webpage.objects.all()
    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)



def insert_access(request):
    pk=int(input('enter pk values of webpage: '))
    a=input('enter author:')
    d=input('enter date: ')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
    NAO.save()
    QLAO=AccessRecord.objects.all()
    d={'QLAO':QLAO}
    return render(request,'display_accessrecord.html',d)




def update_webpage(request):
    QLWO=

    d={'QLWO':QLWO}
    return render(request,'display_webpage.html',d)






    