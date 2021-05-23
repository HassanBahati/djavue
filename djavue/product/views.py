from django.http import Http404
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
# view set - to tell django what to get from the model

from .models import Product
from .serializers import ProductSerializer

 
#viewset for getting latest products to show on front page
class LatestProductsList(APIView):
    def get(self, request, format=None):
        #get 1st 4 products from db
        products = Product.objects.all()[0:4]
        #convert to json (many=true because of more than 1 product)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

#for viewing the details of a product
class ProductDetails(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            # checking if the product exists
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            # raise 404 error if prod doesnt exists 
            raise Http404

    #to overide the get method from above func
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        #using prod serializer to get all the fields
        serializer = ProductSerializer(product)
        return Response(serializer.data)