from django.db import models
from datetime import datetime
# Create your models here.

class Type(models.Model):
	nombre=models.CharField(max_length=150,verbose_name="Nombre")

	def __str__(self):
		return self.nombre

class Categoria(models.Model):
	nombre=models.CharField(max_length=150,verbose_name="categoria")
	def __str__(self):
		return self.nombre


class Empleado(models.Model):
	categ= models.ManyToManyField(Categoria)
	type=models.ForeignKey(Type,on_delete=models.CASCADE)
	nombre=models.CharField(max_length=150,verbose_name="Nombre")
	apellido=models.CharField(max_length=150,verbose_name="Apellido")
	dni=models.IntegerField(unique=True,verbose_name="DNI")
	fecha_de_registro=models.DateField(default=datetime.now, verbose_name="Fecha de Registro")
	fecha_creacion=models.DateTimeField(auto_now=True)
	fecha_actualizacion=models.DateTimeField(auto_now_add=True)
	edad=models.PositiveIntegerField(default=0)
	salario=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
	estado=models.BooleanField(default=True)
	imagen=models.ImageField(upload_to='imagen/%Y/%m/%d', null=True,blank=True)

	def __str__(self):
		return self.nombre, self.apellido