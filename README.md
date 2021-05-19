# GRC_App
URLS are <br>
local/info/{<br>
            urlpatterns = [
    path('corpo/create', createCorporate, name='createcorpo'),
    path('corpo/list/', listCorporate, name='listcorpo'),
    path('corpo/delete/<int:pk>', deleteCorporate, name='deletecorpo'),
    path('corpo/update/<int:pk>', updateCorporate, name='updatecorpo'),
    path('corpo/detail/<int:pk>', detailCorporate, name='detailcorpo'),

    ]
}
