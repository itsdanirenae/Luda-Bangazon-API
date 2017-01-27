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


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    The User View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific User's url for the `update` and `destroy` actions.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    
  

class OrderViewSet(viewsets.ModelViewSet):
    """
    The Order View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Order's url for the `update` and `destroy` actions.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
   

class PaymentMethodViewSet(viewsets.ModelViewSet):
    """
    The Payment Method View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Method's url for the `update` and `destroy` actions.
    """
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    The Product Category View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Category's url for the `update` and `destroy` actions.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer



class ProductOrderViewSet(viewsets.ModelViewSet):
    """
    The Product/Order View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific item's url for the `update` and `destroy` actions.
    """
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer

  

class ProductViewSet(viewsets.ModelViewSet):
    """
    The Product View provides the `list`, `create`, and `retrieve` actions.
    Please click on a specific Product's url for the `update` and `destroy` actions.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


