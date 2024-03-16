from .models import Advert
from django import forms


class AdvertForm(forms.ModelForm):
    """
    Form for user advert upload
    """
    class Meta:
        model = Advert
        fields = ('title', 'image', 'excerpt', 'pet_name',
                  'pet_breed', 'pet_age', 'vaccinated',
                  'description', 'phone',)
