from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include('panel.urls')),
    url(r'^lugar/', include('place.urls')),
    url(r'^proveedor/', include('provider.urls')),
    url(r'^cliente/', include('client.urls')),
]