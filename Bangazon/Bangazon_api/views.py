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

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        user = self.get_object()
        return Response(user.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        order = self.get_object()
        return Response(order.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PaymentMethodViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        paymentMethod = self.get_object()
        return Response(paymentMethod.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        prodCat = self.get_object()
        return Response(prodCat.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductOrderViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        prodOrder = self.get_object()
        return Response(prodOrder.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        product = self.get_object()
        return Response(product.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('UserViewSet', request=request, format=format),
#         'products': reverse('ProductViewSet', request=request, format=format)
#     })