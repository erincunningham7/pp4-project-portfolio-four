from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Advert

class AdList(generic.ListView):
    model = Advert

