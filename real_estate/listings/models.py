from django.db import models
from django.db.models import Model

class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    address = models.CharField(max_length=100)
    # image
    image = models.ImageField()

    def __str__(self):
        return self.title