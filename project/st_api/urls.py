from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'class', class_veiwset)
router.register(r'student', st_veiwset)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('start/',hello,name='hello' ),
    # path('student/',hello,name='hello' ),
]
