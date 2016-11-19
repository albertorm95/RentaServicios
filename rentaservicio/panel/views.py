from django.views.generic.base import TemplateView

class Panel(TemplateView):
	template_name = 'panel/inicio.html'

	def get_context_data(self, **kwargs):
		context = super(Panel, self).get_context_data(**kwargs)
		perfil = False

		if hasattr(self.request.user, 'cliente'):
			perfil = 'cliente'
		elif hasattr(self.request.user, 'proveedor'):
			perfil = 'proveedor'

		context['perfil'] = perfil

		return context