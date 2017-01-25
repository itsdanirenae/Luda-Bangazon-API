from django.conf.urls import url, include
from . import views
from .views import *
"""  
    url configuration for the bangazon_api application
"""


urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^payment-methods/$', PaymentMethodList.as_view()),
    url(r'^payment-methods/(?P<pk>[0-9]+)/$', PaymentMethodDetail.as_view()),
    url(r'^orders/$', OrderList.as_view()),
    url(r'^orders/(?P<pk>[0-9]+)/$', OrderDetail.as_view()),
    url(r'^product-categories/$', ProductCategoryList.as_view()),
    url(r'^product-categories/(?P<pk>[0-9]+)/$', ProductCategoryDetail.as_view()),
    url(r'^products/$', ProductList.as_view()),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetail.as_view()),
    url(r'^product-order/$', ProductOrderList.as_view()),
    url(r'^product-order/(?P<pk>[0-9]+)/$', ProductOrderDetail.as_view()),
]