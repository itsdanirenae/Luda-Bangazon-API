from Bangazon_api.models import *
from Bangazon_api.serializers import *
from rest_framework import generics

class ProductOrderList(generics.ListCreateAPIView):
	"""
	List all product orders, or create a new order
	"""
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer

class ProductOrderDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List all product orders, or create a new order
    """
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
