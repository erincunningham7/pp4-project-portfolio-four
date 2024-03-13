from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField

# Create your models here.

class Advert(models.Model):
    title = models.CharField(max_length=254, unique=True)
    excerpt = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    pet_name = models.CharField(max_length=254, null=False, blank=False)
    pet_breed = models.CharField(max_length=254, null=False, blank=False)
    pet_age = models.IntegerField()
    vaccinated = models.BooleanField(default=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | added by {self.user} on {self.created_on}"
