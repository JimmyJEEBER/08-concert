from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *


# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"
    
@login_required
def test_view(request):
    return render(request, "test.html")

def get_artists(request):
    if request.method == "GET":
        artists=Artists.objects.all()
    return JsonResponse(list(artists.values()), safe=False)

def get_songs(request):
    if request.method == "GET":
        songs=Songs.objects.all()
    return JsonResponse(list(songs.values()), safe=False)   

def get_venues(request):
    if request.method == "GET":
        venues=Venue.objects.all()
    return JsonResponse(list(venues.values()), safe=False)    

def get_concerts(request):
    if request.method == "GET":
        songs=Songs.objects.all()
    return JsonResponse(list(songs.values()), safe=False)   