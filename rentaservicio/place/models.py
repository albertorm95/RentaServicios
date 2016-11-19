from django.db import models

class Place(models.Model):
	name = models.CharField(max_length=250, verbose_name="Nombre del Lugar")
	address = models.TextField(max_length=12, verbose_name="Dirección")
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return "%s" % self.name
