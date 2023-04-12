from django.contrib import admin
from .models import *
class class_details_show(admin.ModelAdmin):
    list_display=['cl','name']
    search_fields=['cl',]
    list_filter=['cl']
    ordering=['cl']
class st_details_show(admin.ModelAdmin):
    list_display=['roll_num','st_id','name','branch','Present','finger_auth','block_student','Class']
    search_fields=['name',]
    list_filter=['Class','branch']
    ordering=['roll_num']

# Register your models here.
admin.site.register(class_details,class_details_show)
admin.site.register(student_details,st_details_show)
