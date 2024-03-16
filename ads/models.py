from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField

# Create your models here.


class Advert(models.Model):
    """
    A model for the essential advert data fields
    """
    title = models.CharField(max_length=254, unique=True)
    excerpt = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = ResizedImageField(
                              size=[300, 300],
                              quality=75,
                              upload_to="media/",
                              force_format='WEBP',
                              blank=True
                              )
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