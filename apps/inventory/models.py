from django.db import models

# Create your models here.
import datetime as d
# Create your models here.

class Item(models.Model):
	title = models.CharField(max_length=50) #when displaying a web page, it will look in folders titled the same as this for this picture
	description = models.CharField(default = "No details yet! Something has probably gone wrong." , max_length = 500)
	price = models.DecimalField(default = 0.00,max_digits = 6, decimal_places = 2)
	date_recieved = models.DateField(default = d.date.today)
	quantity = models.SmallIntegerField(default = 0)
	link = models.URLField(default = "google.com")
	location = models.CharField(default = "unsorted", max_length = 200)
	typeID = models.ForeignKey('Type', on_delete = models.CASCADE, default = 1)
	def __str__(self):
		return self.title


class Type(models.Model):
	title = models.CharField(max_length = 50)
	def __str__(self):
		return self.title
