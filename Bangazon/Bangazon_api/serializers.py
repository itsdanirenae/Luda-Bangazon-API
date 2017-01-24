from rest_framework import serializers
from Bangazon_api.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'date_of_birth')

