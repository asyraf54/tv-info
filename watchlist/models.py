from django.db import models
from django.contrib.auth.models import User
from myList.models import Show

# Create your models here.
class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)