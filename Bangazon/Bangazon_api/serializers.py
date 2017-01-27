from rest_framework import serializers
from Bangazon_api.models import *
from django.contrib.auth import models

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: User
    Sets user serializer to only show sensitive imformation to superusers
    """

    def to_representation(self, obj):
        """
        A Method to filter fields based on user permissions

        Arguments:
        self
        obj
        """
        # get the original representation
        ret = super(UserProfileSerializer, self).to_representation(obj)

        # remove 'url' field if mobile request
        if self.context['request'].user.is_staff:
            return ret
        else:
            ret.pop('date_of_birth')
            ret.pop('created')
            return ret

    class Meta:
        model = UserProfile
        fields = ('id', 'url', 'first_name', 'last_name', 'date_of_birth', 'created')


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
        fields = ('id', 'url','created', 'active', 'payment_method_id', 'user_id',)

        
class PaymentMethodSerializer(serializers.HyperlinkedModelSerializer):
    """
    Class for data serialization of a specific Model: Payment Method
    Sets user serializer to only show sensitive imformation to superusers
    """
    class Meta:
        model = PaymentMethod
        fields = ('id', 'url', 'name', 'account_number', 'user_id',)
        # extra_kwargs = {'account_number': {'write_only': True}}
