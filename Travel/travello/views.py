from django.shortcuts import render
from .models import Destination


def index(request):
    dest = Destination()
    dests = Destination.objects.all()




    return render(request, 'index.html', {'dests': dests})



