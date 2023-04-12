from django.db import models

# Create your models here.
class class_details(models.Model):
    cl=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    def __str__(self):
        return str(self.cl) + " -- " +self.name

class student_details(models.Model):
    st_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    roll_num=models.IntegerField()
    branch=models.CharField(max_length=10,choices=(
        ('ECE','ECE'),
        ('CSE','CSE'),
        ('ME','ME')
    ))
    Present =models.BooleanField(default=True)
    finger_auth =models.BooleanField(default=False)
    block_student =models.BooleanField(default=False)
    Class=models.ForeignKey(class_details, on_delete=models.CASCADE)