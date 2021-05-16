
from GRCmain import settings
from django.urls import path, include
from . import views

urlpatterns = [

    path('', include('django.contrib.auth.urls')),
    path('log/',views.login_view,name='login')
]