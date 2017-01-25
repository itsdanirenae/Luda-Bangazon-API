from Bangazon_api.models import *
from Bangazon_api.serializers import *
from rest_framework import generics


class OrderList(generics.ListCreateAPIView):
    """
    List all Orders, or create a new Order.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    List Order details.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class PaymentMethodList(generics.ListCreateAPIView):
    """ List Product or create a new user
    """
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class PaymentMethodDetail(generics.RetrieveUpdateDestroyAPIView):
    """ List selected product detail
    """

    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class ProductCategoryList(generics.ListCreateAPIView):
    """
    List all Product Categories
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List all products with the selected Product Category
    """
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

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

class ProductList(generics.ListCreateAPIView):
    """ List Product or create a new user
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """ List selected product detail
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user instance.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
