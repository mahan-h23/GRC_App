from django.urls import path
from .views import *

urlpatterns = [
    path('corpo/create', createCorporate, name='createcorpo'),
    path('corpo/list/', listCorporate, name='listcorpo'),
    path('corpo/delete/<int:pk>', deleteCorporate, name='deletecorpo'),
    path('corpo/update/<int:pk>', updateCorporate, name='updatecorpo'),
    path('corpo/detail/<int:pk>', detailCorporate, name='detailcorpo'),

]

