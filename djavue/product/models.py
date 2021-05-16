from django.db import models

# category model
class Cateogry(models.Model):
    name = models.charField(max_length=255)
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



