
from django.urls import path
from .views import *



urlpatterns = [
    path('', viewdash,name = 'dash'),
    path('tech/', techview,name = 'tech'),
    path('marketing/', marketingview,name = 'marketing'),
    path('bd/', bdview,name = 'bd'),
    path('commercial/', coomercial,name = 'commercial'),
    path('cx/', cxview,name = 'cx'),
    path('legal', legalview,name = 'legal'),
    path('finance/', financeview,name = 'finance'),
    path('operation/', operationview,name = 'operation'),
    path('cross/', crossview,name = 'cross'),
    path('hr/', hrview,name = 'hr'),

]
