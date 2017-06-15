
from django.shortcuts import redirect
#from django.http import HttpResponseRedirect
#from siirler.views import siir_list

def redirect_roof(request):
    return redirect('siir_listesu')