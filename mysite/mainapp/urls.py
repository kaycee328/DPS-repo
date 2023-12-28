from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-homepage'),
    path('home/', views.home, name='main-home'),
    path('predict/', views.predict, name='predict'),
    path('result/', views.result, name='result'),
]

