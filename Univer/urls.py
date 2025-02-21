# myapp/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('index', index, name='home'),
    path('category/<int:category_id>/', category_new, name='category')

]
