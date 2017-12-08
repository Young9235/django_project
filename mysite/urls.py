"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#from .views import home1
from .views import Home
from .views import Base
from .views import Team

# from videos.views import home
# from videos.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', home, name='home'),
    #url(r'^$', HomeView.as_view(), name='home'),          #r은 read 읽는 것 / ^$:아무것도 안들어 간것. ^:시작 / $:끝
    url(r'^$', Home.as_view()),
    url(r'^base/$', Base.as_view()),
    url(r'^team/$', Team.as_view()),
    # url(r'^about/$', about),
    # url(r'^team/$', team),
    #url(r'^Team/$', Team.as_view()),
]
