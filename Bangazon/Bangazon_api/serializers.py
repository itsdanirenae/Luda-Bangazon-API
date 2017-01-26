from rest_framework import serializers
from Bangazon_api.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: User
    """
    
    class Meta:
        model = User
        fields = ('id', 'url', 'first_name', 'last_name', 'date_of_birth',)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Product
    """  

    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'description', 'price', 'quantity_available', 'product_category_id', 'user_id',)


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: ProductCategory
    """
    class Meta:
        model = ProductCategory
        fields = ('id', 'url', 'name',)


class ProductOrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: ProductOrder
    """
    class Meta:
        model = ProductOrder
        fields = ('id', 'url', 'product_id', 'order_id',)      
  

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Order
    """
    class Meta:
        model = Order
        fields = ('id', 'url', 'active', 'payment_method_id', 'user_id',)

        
class PaymentMethodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Payment Method
    """
    class Meta:
        model = PaymentMethod
        fields = ('id', 'url', 'name', 'account_number', 'user_id',)
