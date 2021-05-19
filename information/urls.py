from django.urls import path
from .views import *

urlpatterns = [
    path('corpo/create', createCorporate, name='createcorpo'),
    path('corpo/list/', listCorporate, name='listcorpo'),
    path('corpo/delete/<int:pk>', deleteCorporate, name='deletecorpo'),
    path('corpo/update/<int:pk>', updateCorporate, name='updatecorpo'),
    path('corpo/detail/<int:pk>', detailCorporate, name='detailcorpo'),

    path('division/create', createDivision, name='createdivision'),
    path('division/list/', listDivision, name='listdivision'),
    path('division/delete/<int:pk>', deleteDivision, name='deletedivision'),
    path('division/update/<int:pk>', updateDivision, name='updatedivision'),
    path('division/detail/<int:pk>', detailDivision, name='detaildivision'),

    path('owner/create', createOwner, name='createowner'),
    path('owner/list/', listOwner, name='listowner'),
    path('owner/delete/<int:pk>', deleteOwner, name='deleteowner'),
    path('owner/update/<int:pk>', updateOwner, name='updateowner'),
    path('owner/detail/<int:pk>', detailOwner, name='detailowner'),

    path('biz/create', createBiz, name='createbiz'),
    path('biz/list/', listBiz, name='listbiz'),
    path('biz/delete/<int:pk>', deleteBiz, name='deletebiz'),
    path('biz/update/<int:pk>', updateBiz, name='updatebiz'),
    path('biz/detail/<int:pk>', detailBiz, name='detailbiz'),

    path('principal/create', createPrincipal, name='createprincipal'),
    path('principal/list/', listPrincipal, name='listprincipal'),
    path('principal/delete/<int:pk>', deletePrincipal, name='deleteprincipal'),
    path('principal/update/<int:pk>', updatePrincipal, name='updateprincipal'),
    path('principal/detail/<int:pk>', detailPrincipal, name='detailprincipal'),

    path('risk/create', createPrincipal, name='createriskl'),
    path('risk/list/', listPrincipal, name='listrisk'),
    path('risk/delete/<int:pk>', deletePrincipal, name='deleterisk'),
    path('risk/update/<int:pk>', updatePrincipal, name='updaterisk'),
    path('risk/detail/<int:pk>', detailPrincipal, name='detailrisk'),

    path('mitigation/create/<int:pk>', createPrincipal, name='createmitigation'),
    path('mitigation/list/', listPrincipal, name='listmitigation'),
    path('mitigation/delete/<int:pk>', deletePrincipal, name='deletemitigation'),
    path('mitigation/update/<int:pk>', updatePrincipal, name='updatemitigation'),
    path('mitigation/detail/<int:pk>', detailPrincipal, name='detailmitigation'),

]

