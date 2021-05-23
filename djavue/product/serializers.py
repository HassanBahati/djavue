from rest_framework import serializers
 
'''
 serializers get data from db and turn it into json so it can be used in frontend
'''

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    #to configure the product serializer 
    class Meta:
        model = Product
        fields = {
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail"
        }