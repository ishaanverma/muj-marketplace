from django.db.models import Q
from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils.text import slugify
import datetime

# Create your models here.

class Taxi(models.Model):
    title           = models.CharField(max_length=120)
    slug            = models.SlugField(blank=True, unique=True)
    leave_date      = models.DateField(default=datetime.date.today)
    description     = models.TextField()
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('taxi:detail', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Taxi.objects.filter(slug=unique_slug) == True:
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