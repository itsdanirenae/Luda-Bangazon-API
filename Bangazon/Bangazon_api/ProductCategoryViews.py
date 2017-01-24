from Bangazon_api.models import *
from Bangazon_api.serializers import *
from rest_framework import generics


class ProductCategoryList(generics.ListCreateAPIView):
	    """
	    List all Product Categories, or create a new user.
	    """
    queryset = Bangazon_api.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	List all products with the selected Product Category
	"""
    queryset = Bangazon_api.objects.all()
    serializer_class = ProductCategorySerializer