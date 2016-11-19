from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
	name = models.CharField(max_length=250, verbose_name="Nombre Completo")
	phone = models.CharField(max_length=12, verbose_name="Teléfono")
	address = models.TextField(max_length=12, verbose_name="Dirección")
	age = models.IntegerField(verbose_name="Edad")
	email = models.EmailField(verbose_name="Correo Electronico")
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cliente", verbose_name="Usuario")
	agenda = models.ManyToManyField('provider.ProviderPlace', through='ClientProvider', through_fields=('client', 'providerplace'), verbose_name="Relacion Cliente-ProveedorLugar", related_name='servicio_agendado')

	def __str__(self):
		return "%s" % self.name

class ClientProvider(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
	providerplace = models.OneToOneField('provider.ProviderPlace', on_delete=models.CASCADE, verbose_name='Relacion Proveedor-Lugar')

	def __str__(self):
		return "%s %s" % (self.providerplace, self.client)