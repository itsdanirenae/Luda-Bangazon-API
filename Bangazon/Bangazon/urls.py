"""Bangazon URL Configuration


Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from Bangazon_api import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('Bangazon_api.urls')),
    
]
