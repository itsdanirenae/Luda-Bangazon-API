from Bangazon_api.models import *
from Bangazon_api.serializers import *
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    """
    List all users, or create a new user.
    """
    queryset = Bangazon_api.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user instance.
    """
    queryset = Bangazon_api.objects.all()
    serializer_class = UserSerializer