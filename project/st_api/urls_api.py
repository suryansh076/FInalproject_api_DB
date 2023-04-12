
from django.urls import path
from .views_api import *

urlpatterns = [
   path('status/',Student_status.as_view(),name='student'),
#    path('register/',Registerview.as_view(),name='Registerview'),
#    path('logging_out/',logout_user.as_view(),name='logput_user')
]