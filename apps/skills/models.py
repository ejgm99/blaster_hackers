from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50)
    field = models.CharField(max_length=50)
    parent = models.CharField(max_length = 200) #parents can be a list of projects separated via semicolon
