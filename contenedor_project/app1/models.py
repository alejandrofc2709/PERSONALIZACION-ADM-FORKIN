from django.db import models

class AutorBD(models.Model):

    nombre = models.CharField(max_length=100, null=False, blank=False, verbose_name="Nombre")
    fecha_nacimiento = models.DateField(null=False, blank=False, verbose_name="Fecha de nacimiento (dd/mm/yyyy)")
    fecha_fallecimiento = models.DateField(null=True, blank=True, verbose_name="Fecha de fallecimiento (dd/mm/yyyy)")
    profesion = models.CharField(max_length=100, null=True, blank=True, verbose_name="Profesión")
    nacionalidad = models.CharField(max_length=50, null=False, blank=False, verbose_name="Nacionalidad" )

    class Meta():
        db_table = "autor"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


    def __str__(self):
        return f"{self.nombre}"
    
class FraseDB(models.Model):

    cita = models.TextField(max_length=600, null=True, blank=True, verbose_name="Cita")
    autor_fk = models.ForeignKey(AutorBD, on_delete=models.CASCADE, null=False, blank=False, verbose_name="Autor")

    class Meta:
        db_table = "frase"
        verbose_name = "Frase"
        verbose_name_plural = "Frases"

    def __str__(self):
        return f"{self.cita}"