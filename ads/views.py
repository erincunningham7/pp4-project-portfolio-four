from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Advert

class AdList(generic.ListView):
    queryset = Advert.objects.all()
    template_name = "ads/index.html"
    paginate_by = 6

