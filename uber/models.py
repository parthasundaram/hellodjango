from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length = 254)
	last_name = models.CharField(max_length = 254)
	email = models.EmailField(max_length = 254)
	uber_uuid = models.CharField(max_length = 254, primary_key = True)

	def __str__(self):
		return self.first_name + " " + self.last_name

class Ride(models.Model):
	user = models.ForeignKey(User)
	uuid = models.CharField(max_length = 254, primary_key=True)
	request_time = models.DateTimeField()
	product_id = models.CharField(max_length = 254, null = True)
	status= models.CharField(max_length = 254)
	distance = models.FloatField()
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()

	def __str__(self):
		return self.uuid