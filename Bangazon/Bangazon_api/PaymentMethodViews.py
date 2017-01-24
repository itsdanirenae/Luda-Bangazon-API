from Bangazon_api.models import *
from Bangazon_api.serializer import *
from rest_framework import generics

class PaymentMethodList(generics.ListCreateAPIView):
    """ List Product or create a new user
    """
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class PaymentMethodDetail(gnerics.RetreiveUpdateDestoryAPIView):
    """ List selected product detail
    """

    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer