from django.shortcuts import render, get_object_or_404, redirect
from .models import Main


# Create your views here.

def home(request):

    site = Main.objects.filter(pk=1)

    return render(request, 'front/home.html', {'site': site})


    '''
    # use variable to send string  to master page (must add this variable in master header too)
    sitename = "MySite | Home"

    return render(request, 'front/home.html', {'sitename': sitename})
    '''


def about(request):
    sitename = "MySite | About"

    return render(request, 'front/about.html')
