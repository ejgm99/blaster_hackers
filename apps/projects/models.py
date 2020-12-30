# Create your models here.
from django.db import models

class Project(models.Model):
	title = models.CharField(max_length=50) #when displaying a web page, it will look in folders titled the same as this for this picture
	description = models.CharField(default = "No details yet! This is probably just a clever title. Or a wild brainstorm" , max_length = 2000)
	links = models.CharField(default = "https://corgiorgy.com/" , max_length = 100) #not sure if this will stay like this
	img = models.ImageField(default = "static/images/room.jpeg")
	def __str__(self):
		return self.title

class Component(models.Model):
	title = models.CharField(default = "Empty Componenet", max_length = 100)
	description = models.CharField(default = "make better", max_length = 3000)
	projectID = models.ForeignKey('Project', on_delete = models.CASCADE)
	def __str__(self):
		return (self.title)

class Step(models.Model):
	description = models.CharField(default = "make better", max_length = 100)
	projectID = models.ForeignKey('Project' , on_delete = models.CASCADE )
	def __str__(self):
		return str(self.projectID.id) +" "+ str(self.description)
