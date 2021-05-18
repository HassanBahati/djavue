from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models

# category model
class Cateogry(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    #order the categories by name
    class Meta:
        ordering = ('name',)

    #string representation of this obj
    def __str__(self):
        return self.name
    
    #function to get url so that its easier to use
    def get_absolute_url(self):
        return f'/{self.slug}/'

class Product(models.Model):
    #once category deleted, all products in it too
    category = models.ForeignKey(Cateogry, related_name='products', on_delete='models.CASCADE')
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload)