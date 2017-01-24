from rest_framework import serializers
from Bangazon_api.models import *

class UserSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: User
    """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'date_of_birth')

class ProductSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Product
    """
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'product_category_id', 'user_id',)


class ProductCategorySerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: ProductCategory
    """
    class Meta:
        model = ProductCategory
        fields = ('id', 'name',)


class ProductOrderSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: ProductOrder
    """
    class Meta:
        model = ProductOrder
        fields = ('id', 'product_id', 'order_id',)      
  

class OrderSerializer(serializers.ModelSerializer):
    """
    Class for data serialization of a specific Model: Order
    """
    class Meta:
        model = Order
        fields = ('id', 'active', 'payment_method_id', 'user_id',)
