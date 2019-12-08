from django.db import models
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    #pass #password
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
