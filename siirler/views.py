
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404

from django.template import Template, loader

from .models import Sair, Siir

#from .forms import UserForm

def sairs(request):
    return  render(request,
        'siirler/sair_list.html',{'sair_listesi': Sair.objects.all()}
        )


def siir_list(request):
    return  render(request,
        'siirler/siir_list.html',{'siir_listesi': Siir.objects.all()}
        )


def siirin_kendi(request,slug):

    piir = get_object_or_404(
        Siir, slug__iexact=slug)
    pair = get_object_or_404(
        Sair, in_adi=piir.in_sairi)
    paydi = piir.in_kaydi.url
    template = loader.get_template(
        'siirler/siir_in_kendi.html')
    return HttpResponse(template.render({'siir': piir,"sair":pair,"kaydi":paydi}))


def sairin_kendi(request,slug):

    pair = get_object_or_404(
        Sair, slug__iexact=slug)
    piirleri=Siir.objects.filter(slug__contains=pair.slug)


    template = loader.get_template(
        'siirler/sair_in_kendi.html')
    return HttpResponse(template.render({'sair': pair,"siirleri":piirleri}))


# def register(request):
#     registered = False
#     if request.method == 'POST':
#         user_form = UserForm(data=request.POST)
#         if user_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             registered = True
#         else:
#             print(user_form.errors)
#     else:
#         user_form = UserForm()
#     return render(request,'register.html', {'user_form': user_form, 'registered': registered})