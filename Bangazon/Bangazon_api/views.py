from Bangazon_api.models import *
from Bangazon_api.serializers import *
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework import renderers 
from rest_framework import permissions
from django.contrib.auth.models import User




class CustomerViewSet(viewsets.ModelViewSet):
    """
    The User View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific User's url for the `update` and `destroy` actions.
    If user is not a staff, This will be the UserView
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    The Order View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Order's url for the `update` and `destroy` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    
   

class PaymentTypeViewSet(viewsets.ModelViewSet):
    """
    The Payment Method View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Method's url for the `update` and `destroy` actions.
    """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):
    """
    The Product Category View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Category's url for the `update` and `destroy` actions.
    """
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer



class OrderProductViewSet(viewsets.ModelViewSet):
    """
    The Product/Order View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific item's url for the `update` and `destroy` actions.
    """
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer

  

class ProductViewSet(viewsets.ModelViewSet):
    """
    The Product View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Product's url for the `update` and `destroy` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


