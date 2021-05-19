from io import BytesIO
from PIL import Image

from django.core.files import File
from django.db import models
from django.db.models.fields.files import ImageField

# category model
class Category(models.Model):
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
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null= True)
    date_added = models.DateTimeField(auto_now_add=True)

    #order the categories by name
    class Meta:
        #- for ascending order
        ordering = ('-date_added',)

    #string representation of this obj
    def __str__(self):
        return self.name
    
    #function to get url so that its easier to use
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    #check if the image exists 
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url 
        return ''
    
    #check if thumbnail exists if not create  
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http:127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return 'http:127.0.0.1:8000' +self.thumbnail.url
                
            #if product has no image return empty string
            else:
                return ''

    #make_thumbnail function
    def make_thumbnail(self, image, size=(300,200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

