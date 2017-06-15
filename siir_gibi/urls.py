"""siir_gibi URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

from siirler import urls as siirler_urls
from okumalar import urls as okumalar_urls


from .views import redirect_roof

urlpatterns = [
    url(r'^$', redirect_roof),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^okumalar/', include(okumalar_urls)),
    url(r'^', include(siirler_urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),

] 
