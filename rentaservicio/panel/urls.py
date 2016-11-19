from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Panel.as_view(), name='panel-inicio')
]