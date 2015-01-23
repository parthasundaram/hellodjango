from django.db import models

# Create your models here.
class Business(models.Model):
	business_name = models.CharField(max_length = 254)
	address1 = models.CharField(max_length = 254)
	address2 = models.CharField(max_length = 254)
	address3 = models.CharField(max_length = 254)
	city = models.CharField(max_length = 254)
	country = models.CharField(max_length = 254)
	phone = models.CharField(max_length = 254)
	postal_code = models.CharField(max_length = 254)
	state = models.CharField(max_length = 254)
	yelp_business_id = models.CharField(max_length = 254)

	def __str__(self):
		return self.business_name 