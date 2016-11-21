from django.db import models
from django.contrib.auth.models import User

class Provider(models.Model):
	name = models.CharField(max_length=250, verbose_name="Nombre Completo")
	phone = models.CharField(max_length=12, verbose_name="Teléfono")
	address = models.TextField(verbose_name="Dirección")
	age = models.IntegerField(verbose_name="Edad")
	email = models.EmailField(verbose_name="Correo Electronico")
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="proveedor", verbose_name="Usuario")
	places = models.ManyToManyField('place.Place', through='ProviderPlace', related_name='horarios', through_fields=('provider', 'place'), verbose_name="Lugares")
	specialty = models.ManyToManyField('Specialty', related_name='especialidades', verbose_name='Especialidades')

	def __str__(self):
		return "%s" % self.name

class Specialty(models.Model):
	name = models.CharField(max_length=30, verbose_name='Nombre Especialidad')
	def __str__(self):
		return "%s" % self.name

class ProviderPlace(models.Model):
	DAYSOFWEEK = (
		('Lunes', 'Lunes'),
		('Martes', 'Martes'),
		('Miercoles', 'Miercoles'),
		('Jueves', 'Jueves'),
		('Viernes', 'Viernes'),
		('Sabado', 'Sabado'),
		('Domingo', 'Domingo')
	)

	HOUROFDAY = (
		('01:00:00', '1:00-2:00'),
		('02:00:00', '2:00-3:00'),
		('03:00:00', '3:00-4:00'),
		('04:00:00', '4:00-5:00'),
		('05:00:00', '5:00-6:00'),
		('06:00:00', '6:00-7:00'),
		('07:00:00', '7:00-8:00'),
		('08:00:00', '8:00-9:00'),
		('09:00:00', '9:00-10:00'),
		('10:00:00', '10:00-11:00'),
		('11:00:00', '11:00-12:00'),
		('12:00:00', '12:00-13:00'),
		('13:00:00', '13:00-14:00'),
		('14:00:00', '14:00-15:00'),
		('15:00:00', '15:00-16:00'),
		('16:00:00', '16:00-17:00'),
		('17:00:00', '17:00-18:00'),
	)

	provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name='Proveedor')
	place = models.ForeignKey('place.Place', on_delete=models.CASCADE, verbose_name='Lugar')
	day = models.CharField(max_length=10, choices=DAYSOFWEEK, default='l', verbose_name='Dia de la semana')
	service_time = models.CharField(max_length=8, choices=HOUROFDAY, default='08:00:00', verbose_name='Hora de Servicio')

	def __str__(self):
		return "%s %s" % (self.provider, self.place)