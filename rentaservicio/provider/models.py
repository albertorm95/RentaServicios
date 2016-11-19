from django.db import models
from django.contrib.auth.models import User

class Provider(models.Model):
	name = models.CharField(max_length=250, verbose_name="Nombre Completo")
	phone = models.CharField(max_length=12, verbose_name="Teléfono")
	address = models.TextField(max_length=12, verbose_name="Dirección")
	age = models.IntegerField(verbose_name="Edad")
	email = models.EmailField(verbose_name="Correo Electronico")
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="proveedor", verbose_name="Usuario")
	places = models.ManyToManyField('place.Place', through='ProviderPlace', through_fields=('provider', 'place'), related_name='lugares', verbose_name="Lugares")
	specialty = models.ManyToManyField('Specialty', related_name='especialidades', verbose_name='Especialidades')

	def __str__(self):
		return "%s" % self.name

class Specialty(models.Model):
	name = models.CharField(max_length=30, verbose_name='Nombre Especialidad')
	def __str__(self):
		return "%s" % self.name

class ProviderPlace(models.Model):
	DAYSOFWEEK = (
		('l', 'Lunes'),
		('m', 'Martes'),
		('i', 'Miercoles'),
		('j', 'Jueves'),
		('v', 'Viernes'),
		('s', 'Sabado'),
		('d', 'Domingo')
	)

	HOUROFDAY = (
		('8:00', '8:00-9:00'),
		('9:00', '9:00-10:00'),
		('10:00', '10:00-11:00'),
	)

	provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name='Proveedor')
	place = models.ForeignKey('place.Place', on_delete=models.CASCADE, verbose_name='Lugar')
	day = models.CharField(max_length=2, choices=DAYSOFWEEK, default='l', verbose_name='Dia de la semana')
	service_time = models.TimeField(choices=HOUROFDAY, default='8:00', verbose_name='Hora de Servicio')

	def __str__(self):
		return "%s %s" % (self.provider, self.place)