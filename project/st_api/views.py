from django.shortcuts import render
from  rest_framework import routers, serializers, viewsets
from .models import *
from .serielizer import *


# Create your views here.
class class_veiwset(viewsets.ModelViewSet):
    queryset=class_details.objects.all()
    serializer_class=class_seri
class st_veiwset(viewsets.ModelViewSet):
    queryset=student_details.objects.all()
    serializer_class=st_seri
def hello(request):
    return render(request,'student.html')
def finger_auth(request):
    pass