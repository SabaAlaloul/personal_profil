from django.db import models

# Create your models here.
class project(models.Model):
    title = models.CharField(max_length=100)
    decrption = models.TextField()
    techonelogy = models.CharField(max_length=20)
    image = models.FilePathField(path="/img")