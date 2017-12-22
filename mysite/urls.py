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
from django.conf.urls import url, include
from django.contrib import admin
#from .views import home1
from .views import Home
from .views import Base
from .views import Team
from videos.views import VideoListView
from videos.views import VideoDetailView
from videos.views import VideoCreateView, VideoUpdateView, VideoDeleteView
from .views import Landingpage, UserCreateView, UserCreateDoneView


# from videos.views import home
# from videos.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/done/$', UserCreateDoneView.as_view(), name='register_done'),
    #url(r'^$', home, name='home'),
    #url(r'^$', HomeView.as_view(), name='home'),          #r은 read 읽는 것 / ^$:아무것도 안들어 간것. ^:시작 / $:끝
    url(r'^$', Home.as_view()),
    url(r'^base/$', Base.as_view()),
    url(r'^team/$', Team.as_view()),
    # url(r'^about/$', about),
    # url(r'^team/$', team),
    url(r'^video/$', VideoListView.as_view(), name='video'),
    url(r'^video/(?P<pk>\d+)/$', VideoDetailView.as_view(), name='video-detail'),
    url(r'^video/create/$', VideoCreateView.as_view(), name='video-create'),
    url(r'^video/(?P<pk>\d+)/update/$', VideoUpdateView.as_view(), name='video-update'),
    url(r'^video/(?P<pk>\d+)/delete/$', VideoDeleteView.as_view(), name='video-delete'),
    url(r'^index/$', Landingpage.as_view()),
    url(r'^photo/', include("photo.urls", namespace='photo'))
]
