from django.shortcuts import render
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