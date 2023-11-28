from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, TeamMembers


# Create your views here.
def home(request):
    return HttpResponse("home")


def about(request):
    return render(request, "about.html")


def contact(request):
    return HttpResponse("Contact")


def detail(request):
    return render(request, "detail.html")


def thanks(request):
    return HttpResponse("Thanks")


def demo(request):
    obj = Place.objects.all()
    obj1 = TeamMembers.objects.all()
    return render(request, 'index.html', {'result': obj,'members': obj1})
