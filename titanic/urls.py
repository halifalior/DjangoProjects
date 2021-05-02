from django.urls import path
from . import views


urlpatterns = [
    path('', views.home,name='home'),
    path('result/', views.result,name='result'),
    path('home1', views.home1, name='home1'),
    path('result1/', views.result1, name='result1'),
    path('test/', views.test, name='test'),
]
