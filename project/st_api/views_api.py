from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import login, logout,authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *

def hello11(request):
    return render(request,'student.html')

class Student_status(APIView):
    def patch(self,request):
        print('---------    welcome')
        response={}
        response['status']=500
        response['message']=""
        try:
            data=request.data
            if data.get('name') is None:
                response['message']='username is empty'
                raise Exception('Key is not found')
            if data.get('rollnum') is None:
                response['message']='roll number is empty'
                raise Exception('roll num is not found')
            check_student=student_details.objects.filter(roll_num=data.get('rollnum')).first()
            if check_student:
                print("--------------- ",check_student.name)
                print(data.get('status'),check_student.block_student,check_student.finger_auth )
                if (check_student.finger_auth):
                    if data.get('status') and not check_student.block_student:
                        print("----- welcome in if")
                        check_student.Present=True
                        check_student.save()
                    elif not data.get('status') and not check_student.block_student:
                        print("----- welcome in elif")
                        check_student.Present=False
                        check_student.block_student=True
                        check_student.save()
                        response['message']='You are absent and blocked from this class contact your faculty to attend this class'
     
                    else:
                        print("----- welcome in else")
                        response['message']='You are absent and blocked from this class contact your faculty to attend this class'
                        
                else:
                    response['message']='You are not authentcated first authenticate with your fingerperint'
            else:
                    
                response['message']='Invalid User'
                raise Exception('roll num is not found')
            
        except Exception as e:
            print(e)
        return Response(response)

