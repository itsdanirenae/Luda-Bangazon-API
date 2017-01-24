from rest_framework import serializers
from Bangazon_api.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'date_of_birth')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'product_category_id', 'user_id',)

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ('id', 'product_id', 'order_id',)      
  

class OrderSerializer(serializers.ModelSerializer):
    """
    class to serialize order
    """
    class Meta:
        model = Order
        fields = ('id', 'active', 'payment_method_id', 'user_id',)
        
class PaymentMethod(serializers.ModelSerializer):
	class Meta:
		model = PaymentMethod
		fields = ('id','name', 'account-number', 'user_id',)
