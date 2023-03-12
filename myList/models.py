from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    time_publish = models.DateTimeField()
    genre = models.CharField(max_length=150)
    poster_url = models.CharField(max_length=255)
    trailer_url = models.CharField(max_length=255)

