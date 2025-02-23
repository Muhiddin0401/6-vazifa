# myapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index, name='home'),
    path('kompaniya/<int:kompaniya_id>/', komp_avto, name='kompaniya'),
    path('avtomabil/<int:avtomabil_id>/', avtomabil_detail, name='avtomabil_detail'),
]
