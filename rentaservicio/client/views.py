from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import ClientProvider

@method_decorator(login_required, name='dispatch')
class ClientProviderCreate(CreateView):
	""" Crear relacion de Cliente con Provedor """
	template_name = 'client/clientprovider_create.html'		
	success_url = reverse_lazy('panel-inicio')
	model = ClientProvider
	fields = [
		'providerplace'
	]

	def form_valid(self, form):
		form.instance.client = self.request.user.cliente
		response = super(ClientProviderCreate, self).form_valid(form)
		return response


@method_decorator(login_required, name='dispatch')
class ClientProviderDetail(DetailView):
	""" Detalle de la relacion Cliente con Provedor """
	template_name = 'client/clientprovider_detail.html'	
	model = ClientProvider


@method_decorator(login_required, name='dispatch')
class ClientProviderDelete(DeleteView):
	""" Eliminar relacion de Cliente con Provedor """
	template_name = 'client/clientprovider_delete.html'
	success_url = reverse_lazy('panel-inicio')
	model = ClientProvider

@method_decorator(login_required, name='dispatch')
class ClientProviderList(ListView):
	""" Lista relacion de Cliente con Provedor """
	template_name = 'client/clientprovider_list.html'
	success_url = reverse_lazy('panel-inicio')
	model = ClientProvider

	def get_queryset(self):
		return ClientProvider.objects.filter(client=self.request.user.cliente)
