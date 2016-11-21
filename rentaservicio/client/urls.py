from django.conf.urls import url
from . import views

urlpatterns = [	
	url(r'^agendar/$', views.ClientProviderCreate.as_view(), name='clientprovider-create'),
	url(r'^agenda/eliminar/(?P<pk>[0-9]+)/$', views.ClientProviderDelete.as_view(), name='clientprovider-delete'),
	url(r'^agenda/detalle/(?P<pk>[0-9]+)/$', views.ClientProviderDetail.as_view(), name='clientprovider-detail'),
	url(r'^agenda/$', views.ClientProviderList.as_view(), name='clientprovider-list'),
]