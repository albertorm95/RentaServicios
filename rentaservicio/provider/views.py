from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Provider, ProviderPlace
from .forms import ClientProviderForm

@method_decorator(login_required, name='dispatch')
class ProviderDetail(DetailView):
	""" Lista de proveedores """
	template_name = 'provider/provider_detail.html'	
	model = Provider

	def get_context_data(self, **kwargs):
		context = super(ProviderDetail, self).get_context_data(**kwargs)
		context['schedule'] = self.object.providerplace_set.all()
		return context

@method_decorator(login_required, name='dispatch')
class ProviderPlaceDetail(DetailView):
	""" Lista de ProviderPlace """
	template_name = 'provider/providerplace_detail.html'	
	model = ProviderPlace

	def get_context_data(self, **kwargs):
		context = super(ProviderPlaceDetail, self).get_context_data(**kwargs)
		context['form'] = ClientProviderForm(initial={'providerplace' : self.object})
		return context
