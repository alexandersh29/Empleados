from django.db import models

# Create your models here.
class Empleados(models.Model): #Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True, verbose_name="Clave")
    nombre = models.CharField(max_length=30, verbose_name="Nombres") 
    apellido= models.CharField(max_length=20, verbose_name="Apellidos") 
    area= models.CharField(max_length=20, verbose_name="Área") 
    cargo = models.CharField(max_length=20, verbose_name="Cargo") 
    adicional = models.TextField(max_length=20, verbose_name="Información Adicional") 
    imagen = models.FileField(null=True, upload_to="fotos", blank=True,verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")  # Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["created"]
    
    def __str__(self):
        return self.nombre