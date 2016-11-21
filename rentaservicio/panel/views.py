from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from client import models as client_models
from provider import models as provider_models

@method_decorator(login_required, name='dispatch')
class Panel(TemplateView):
	""" Vista del panel """

	template_name = 'panel/home.html'

	def get_context_data(self, **kwargs):
		context = super(Panel, self).get_context_data(**kwargs)
		perfil = False

		if hasattr(self.request.user, 'cliente'):
			perfil = 'cliente'
			context['providers'] = provider_models.Provider.objects.all()

		elif hasattr(self.request.user, 'proveedor'):
			perfil = 'proveedor'

			# lista de clientes agendados
			context['agenda'] = client_models.ClientProvider.objects.filter(providerplace__provider=self.request.user.proveedor)

		context['perfil'] = perfil

		return context


@method_decorator(login_required, name='dispatch')
class InitializeProfile(CreateView):
	""" Crear perfil dependiendo del tipo qu ese especifique en
	la url y asignarlo a usuario """

	template_name = 'panel/init_profile.html'
	success_url = reverse_lazy('panel-inicio')
	model = client_models.Client
	fields = [
		'name',
		'age',
		'email',
		'phone',
		'address',		
	]

	def dispatch(self, request, *args, **kwargs):
		oa = kwargs['type']

		if oa == "client":
			self.model = client_models.Client
			self.model_type = oa		
		elif oa == "provider":
			self.model = provider_models.Provider
			self.model_type = oa

		return super(InitializeProfile, self).dispatch(request, *args, **kwargs)


	def form_valid(self, form):
		form.instance.user = self.request.user
		response = super(InitializeProfile, self).form_valid(form)
		return response
	
	def get_context_data(self, **kwargs):
		context = super(InitializeProfile, self).get_context_data(**kwargs)
		
		if hasattr(self, 'model_type'):
			context['type'] = self.model_type

		return context


@method_decorator(login_required, name='dispatch')
class UpdateUserProfile(UpdateView):
	""" Actualizar perfil de usuario """

	template_name = "panel/profile.html"	
	success_url = reverse_lazy('profile')
	fields = [
		'name',
		'age',
		'email',
		'phone',
		'address',				
	]

	def get_object(self, queryset=None):
		# devolver el perfil correspondiente
		user = self.request.user
		if hasattr(user, 'cliente'):
			return user.cliente
		elif hasattr(user, 'proveedor'):
			self.fields.append('specialty')
			return user.proveedor

		return None

	def get_context_data(self, **kwargs):
		context = super(UpdateUserProfile, self).get_context_data(**kwargs)

		# si el perfil es del proveedor devolver
		# lista de las especialidades
		user = self.request.user
		if hasattr(user, 'proveedor'):
			context['provider'] = True			
			context['places'] = user.proveedor.providerplace_set.all()

		return context

@method_decorator(login_required, name='dispatch')
class CreateSpecialty(CreateView):
	""" Crear especialidad """

	template_name = 'panel/specialty_create.html'
	success_url = reverse_lazy('profile')
	model = provider_models.Specialty
	fields = ['name']


@method_decorator(login_required, name='dispatch')
class ListItemSchedule(ListView):
	""" Lista item de horario """
	template_name = 'schedule/item_list.html'	
	model = provider_models.ProviderPlace

	def get_queryset(self):
		return self.model.objects.filter(provider=self.request.user.proveedor)

@method_decorator(login_required, name='dispatch')
class CreateItemSchedule(CreateView):
	""" Crear item de horario """

	template_name = 'schedule/item_form.html'
	success_url = reverse_lazy('schedule-item-list')
	model = provider_models.ProviderPlace
	fields = [
		'place',
		'day',
		'service_time',
	]

	def form_valid(self, form):
		form.instance.provider = self.request.user.proveedor
		response = super(CreateItemSchedule, self).form_valid(form)
		return response

@method_decorator(login_required, name='dispatch')
class UpdateItemSchedule(UpdateView):
	""" Actualizar item de horario """

	template_name = 'schedule/item_form.html'
	success_url = reverse_lazy('schedule-item-list')
	model = provider_models.ProviderPlace
	fields = [
		'place',
		'day',
		'service_time',
	]

@method_decorator(login_required, name='dispatch')
class DeleteItemSchedule(DeleteView):
	template_name = 'schedule/item_delete.html'
	success_url = reverse_lazy('schedule-item-list')
	model = provider_models.ProviderPlace