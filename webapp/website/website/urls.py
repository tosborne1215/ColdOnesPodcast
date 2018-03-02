"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from . import views
from podcast.podcast_feed import PodcastFeed

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls', namespace="blog", app_name="blog")),
    url(r'^podcast/', include('podcast.urls',
        namespace="podcast", app_name="podcast")),
    url(r'^podcast.rss$', PodcastFeed(), name='podcastfeed'),
    url(r'^contactus', views.ContactUsView.as_view(), name='contactus'),
    url(r'^forum', views.ForumView.as_view(), name='forum'),
    url(r'^legal', views.LegalView.as_view(), name='legal'),
    url(r'^privacypolicy', views.PrivacyPolicyView.as_view(),
        name='privacypolicy'),
    url(r'^search', views.SearchView.as_view(), name='search'),
    url(r'^about', views.AboutView.as_view(), name='about'),
    url(r'^$', views.IndexView.as_view(), name='index'),
]
