from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
	title 			= models.CharField(max_length=120)
	slug 			= models.SlugField(blank=True, unique=True)
	description 	= models.TextField()
	price			= models.DecimalField(decimal_places=2, max_digits=10, default=10.00)
	image 			= models.ImageField(upload_to="products/", null=True, blank=True)
	active 			= models.BooleanField(default=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('products:detail', kwargs={'slug': self.slug})

	def __str__(self):
		return self.title
