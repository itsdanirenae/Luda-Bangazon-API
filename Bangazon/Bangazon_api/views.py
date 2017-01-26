from Bangazon_api.models import *
from Bangazon_api.serializers import *
from rest_framework import generics
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework import renderers 



class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

  

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
   

class PaymentMethodViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer



class ProductOrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer

  

class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # serializer = ProductSerializer(queryset, context={'request': request})




# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('UserViewSet', request=request, format=format),
#         'products': reverse('ProductViewSet', request=request, format=format)
#     })