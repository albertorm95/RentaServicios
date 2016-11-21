from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.Panel.as_view(), name='panel-inicio'),
	url(r'^especialidad/agregar/$', views.CreateSpecialty.as_view(), name='specialty-create'),
	url(r'^horario/eliminar/(?P<pk>[0-9]+)/$', views.DeleteItemSchedule.as_view(), name='schedule-item-delete'),
	url(r'^horario/agregar/$', views.CreateItemSchedule.as_view(), name='schedule-item-create'),
	url(r'^horario/actualizar/(?P<pk>[0-9]+)/$', views.UpdateItemSchedule.as_view(), name='schedule-item-update'),	
	url(r'^horario/$', views.ListItemSchedule.as_view(), name='schedule-item-list'),	
	url(r'^perfil/(?P<type>[-\w]+)/$', views.InitializeProfile.as_view(), name='profile-init'),
	url(r'^perfil/$', views.UpdateUserProfile.as_view(), name='profile'),	
]