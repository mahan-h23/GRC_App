"""GRCmain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from mainpage import urls as urlmain
from accounts import urls as urlaccount
from risks_mitigations import urls as riskurls
from indicators import urls as indicatorsurls
from . import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(urlmain)),
    path('account/',include(urlaccount)),
    path('indicators/',include(indicatorsurls)),

    path('add/',include(riskurls))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
