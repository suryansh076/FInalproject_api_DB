from rest_framework import serializers
from .models import *

class class_seri(serializers.HyperlinkedModelSerializer):
    cl=serializers.ReadOnlyField()
    class Meta:
        model=class_details
        fields='__all__'
class st_seri(serializers.HyperlinkedModelSerializer):
    st_id=serializers.ReadOnlyField()
    class Meta:
        model=student_details
        fields='__all__'
