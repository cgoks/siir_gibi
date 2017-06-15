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
from django.conf.urls import url

from siirler.views import sairs, siir_list, siirin_kendi, sairin_kendi

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r"^sairler/$",sairs, name="sair_listesu"),
    url(r"^siirler/$",siir_list, name="siir_listesu"),
    url(r"^siirler/(?P<slug>[\w\-]+)/$", siirin_kendi,name="siirin_kendu"),
    url(r"^sairler/(?P<slug>[\w\-]+)/$", sairin_kendi,name="sairin_kendu"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
