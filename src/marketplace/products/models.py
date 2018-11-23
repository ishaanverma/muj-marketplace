from django.db.models import Q
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify

class Category(models.Model):
	name = models.CharField(max_length=120, unique=True)
	slug = models.SlugField(blank=True, unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)

	def _get_unique_slug(self):
		slug = slugify(self.name)
		unique_slug = slug
		num = 1
		while Category.objects.filter(slug=unique_slug) == True:
			unique_slug = '%s-%d' % (slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.id:
			if not self.slug:
				self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

class ProductQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

	def featured(self):
		return self.filter(featured=True)

	def search(self, query):
		lookups = (Q(title__icontains=query) |
					Q(description__icontains=query) |
					Q(category__name__icontains=query))
		return self.filter(lookups).distinct()

class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def all(self):
		return self.get_queryset().active()

	def featured(self):
		return self.get_queryset().featured()

	def search(self, query):
		return self.get_queryset().active().search(query)

class Product(models.Model):
	title 			= models.CharField(max_length=120)
	slug 			= models.SlugField(blank=True, unique=True)
	description 	= models.TextField()
	price			= models.DecimalField(decimal_places=2, max_digits=10, default=10.00)
	image 			= models.ImageField(upload_to="products/", null=True, blank=True)
	active 			= models.BooleanField(default=True)
	featured		= models.BooleanField(default=False)
	timestamp 		= models.DateTimeField(auto_now_add=True)
	user 			= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	category 		= models.ForeignKey(Category, on_delete=models.PROTECT)

	objects = ProductManager()

	def get_absolute_url(self):
		return reverse('products:detail', kwargs={'slug': self.slug})

	def _get_unique_slug(self):
		slug = slugify(self.title)
		unique_slug = slug
		num = 1
		while Product.objects.filter(slug=unique_slug).exists():
			unique_slug = '%s-%d' % (slug, num)
			num += 1
		return unique_slug

	def save(self, *args, **kwargs):
		if not self.id:
			if not self.slug:
				self.slug = self._get_unique_slug()
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title
