from django.urls import path
from .views import *



urlpatterns = [
    path('risk/', riskView,name= 'riskadd'),
    path('mitigation/<str:pk>',mitigationView , name = 'mitigation'),
    path('test/<int:pk>/',sqlq , name = 'test'),
    path('detail/<str:pk>/',riskDetail , name = 'detail'),
    path('get/<int:pk>/',grtfile , name = 'getfile'),
    path('update/<int:pk>/',riskUpdate , name = 'update')


]