from django.urls import path
from . import views

urlpatterns = [
    # FBVs
    # path('', views.home, name='homepage'),
    # path('predict/', views.predict, name='predict'),
    # path('result/', views.result, name='result'),

    # CBVs
    path('home/', views.HomePage.as_view(), name='homepage'),
    path('', views.HomePage.as_view(), name='home'),
    path('test/questions/', views.predictionform, name='test'),
    # path('test/questions/', views.Predict.as_view(), name='test'),
    path('user-result/', views.ResultView.as_view(), name='output'),
]

