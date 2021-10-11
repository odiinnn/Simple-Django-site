from django.urls import path, include
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='home'),
    path('join', views.join, name='join')
]