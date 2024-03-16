from django.contrib import admin
from .models import Advert
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Advert)
class AdvertAdmin(SummernoteModelAdmin):

    list_display = ('user', 'pet_name', 'created_on',)
    search_fields = ['title', 'pet_name', 'pet_breed', 'description', ]
    list_filter = ('vaccinated', 'created_on', 'pet_breed',)
    summernote_fields = ('description',)
