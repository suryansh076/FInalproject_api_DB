from django.contrib import admin
from .models import *
class class_details_show(admin.ModelAdmin):
    list_display=['cl','name']
    search_fields=['cl',]
    list_filter=['cl']
    ordering=['cl']
class st_details_show(admin.ModelAdmin):
    list_display=['st_id','name','roll_num','branch','Persent','Class']
    search_fields=['name',]
    list_filter=['Class','branch']
    ordering=['st_id']

# Register your models here.
admin.site.register(class_details,class_details_show)
admin.site.register(student_details,st_details_show)
