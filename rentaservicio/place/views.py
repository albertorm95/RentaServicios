from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Place

@method_decorator(login_required, name='dispatch')
class PlaceList(ListView):
	""" Lista de lugares """
	template_name = 'place/place_list.html'	
	model = Place	

@method_decorator(login_required, name='dispatch')
class CreatePlace(CreateView):
	""" Crear lugar """
	template_name = 'place/place_form.html'
	success_url = reverse_lazy('places-list')
	model = Place
	fields = [
		'name',
		'address',
		'price',
	]

@method_decorator(login_required, name='dispatch')
class UpdatePlace(UpdateView):
	""" Actualizar lugar """
	template_name = "place/place_form.html"	
	success_url = reverse_lazy('places-list')
	model = Place
	fields = [
		'name',
		'address',
		'price',
	]

@method_decorator(login_required, name='dispatch')
class DeletePlace(DeleteView):
	""" Eliminar lugar """
	template_name = "place/place_delete.html"	
	success_url = reverse_lazy('places-list')
	model = Place
