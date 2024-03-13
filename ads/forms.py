from .models import Advert
from django import forms


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ('title', 'featured_image', 'excerpt', 'pet_name', 'pet_breed', 'pet_age', 'vaccinated', 'description', 'phone',)