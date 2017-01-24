from Bangazon_api.models import *
from Bangazon_api.serializer import *
from rest_framework import generics

class ProductList(generics.ListCreateAPIView):
    """ List Product or create a new user
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(gnerics.RetreiveUpdateDestoryAPIView):
    """ List selected product detail
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer