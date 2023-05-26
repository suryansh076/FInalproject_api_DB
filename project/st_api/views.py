import json
from django.shortcuts import render,HttpResponse
from  rest_framework import routers, serializers, viewsets
from .models import *
from .serielizer import *
from rest_framework.response import Response

# Create your views here.
class class_veiwset(viewsets.ModelViewSet):
    queryset=class_details.objects.all()
    serializer_class=class_seri
class st_veiwset(viewsets.ModelViewSet):
    queryset=student_details.objects.all()
    serializer_class=st_seri

    #cls = class_details.objects.filter(id=serializer_class.data['Class'])
def hello(request):
    return render(request,'student.html')
def finger_auth(request,roll):
    myroll=student_details.objects.filter(roll_num=roll).first()
    if(myroll):
        print("updated")
        myroll.finger_auth=True
        myroll.save()
    return HttpResponse("")