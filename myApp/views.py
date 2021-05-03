from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _

# Create your views here.
def home(request):
    return render(request, 'home.html')

def home2(request):
    return render(request, 'home2.html')