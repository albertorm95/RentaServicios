from django.conf.urls import url
from . import views

urlpatterns = [	
	url(r'^agregar/$', views.CreatePlace.as_view(), name='places-create'),
	url(r'^actualizar/(?P<pk>[0-9]+)/$', views.UpdatePlace.as_view(), name='places-update'),
	url(r'^delete/(?P<pk>[0-9]+)/$', views.DeletePlace.as_view(), name='places-delete'),
	url(r'^$', views.PlaceList.as_view(), name='places-list'),
]