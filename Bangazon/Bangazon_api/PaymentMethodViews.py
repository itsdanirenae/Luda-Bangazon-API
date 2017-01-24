from Bangazon_api.models import *
from Bangazon_api.serializer import *
from rest_framework import generics

class PaymentList(generics.ListCreateAPIView):
    """ List Product or create a new user
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentMethodSerializer

class PaymentDetail(gnerics.RetreiveUpdateDestoryAPIView):
    """ List selected product detail
    """

    queryset = Payment.objects.all()
    serializer_class = PaymentMethodSerializer