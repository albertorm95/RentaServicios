from django.conf.urls import url
from . import views

urlpatterns = [		
	url(r'^detalle/(?P<pk>[0-9]+)/$', views.ProviderDetail.as_view(), name='provider-detail'),
	url(r'^place/(?P<pk>[0-9]+)/$', views.ProviderPlaceDetail.as_view(), name='providerplace-detail'),
]