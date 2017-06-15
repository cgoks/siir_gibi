from django.contrib import admin

# Register your models here.
from siirler.models import Sair, Kitap, Siir
from okumalar.models import Okuma

admin.site.register(Sair)
admin.site.register(Siir)
admin.site.register(Kitap)
admin.site.register(Okuma)