from django.conf.urls import url, include
from . import views
from .views import *

urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^payment-methods/$', PaymentMethodList.as_view()),
    url(r'^orders/$', OrderList.as_view()),
    url(r'^product-categories/$', ProductCategoryList.as_view()),
    url(r'^products/$', ProductList.as_view()),
    url(r'^product-order/$', ProductOrderList.as_view()),
]