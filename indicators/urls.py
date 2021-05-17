from django.urls import path

from .views import *


urlpatterns = [
    path('',viewList,name='indicators'),
    path('detail/',detailVew,name = 'detailindicator')

]