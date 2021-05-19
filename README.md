# GRC_App
URLS are <br>
local/info/{<br>
            urlpatterns = [<br>
    path('corpo/create', createCorporate, name='createcorpo'),<br>
    path('corpo/list/', listCorporate, name='listcorpo'),<br>
    path('corpo/delete/<int:pk>', deleteCorporate, name='deletecorpo'),<br>
    path('corpo/update/<int:pk>', updateCorporate, name='updatecorpo'),<br>
    path('corpo/detail/<int:pk>', detailCorporate, name='detailcorpo'),<br>

    ]
}
