from django.conf.urls import url, include
from . import views
from .views import *

urlpatterns = [
    url(r'^users/$', UserList),
]