from django.contrib import admin
from .models import AutorBD, FraseDB

# admin sirve para configurar el panel de administración de Django, 
# donde se pueden gestionar los modelos de la aplicación. 
# Para que un modelo sea visible en el panel de administración, es necesario registrarlo aquí.

admin.site.site_header = "Panel de administración de autores y frases" # prsonalizar el header del admin

admin.site.index_title = "Mis aplicaciones" # personalizar el index del admin

class FraseInLine(admin.TabularInline):
    model = FraseDB
    extra = 2 # Cant de formularios q permitira crear smiultaneamente desde el autor

class AutorAdmin(admin.ModelAdmin):
    # Estos son los campos que podemos gestonar desde el admin
    fields = ["nombre", "fecha_nacimiento", "fecha_fallecimiento", "profesion", "nacionalidad"]

    # Estos son los campos que se muestran cuando entramos en la entrada de un modelo
    list_display = ["nombre", "fecha_nacimiento", "fecha_fallecimiento"]

    # Campos para permitir el inline
    inlines = [FraseInLine]

    # Accion personalizada 
    def calcularDiasvivo(self, request, queryset):
        autores: list[AutorBD] = queryset.all() # obtenemos los autores
        for autor in autores:
            if autor.fecha_fallecimiento is None:
                self.message_user(request=request, message=f"{autor} aún vive")
                continue
            tiempoVivo = autor.fecha_fallecimiento - autor.fecha_nacimiento
            self.message_user(request=request, message=f"{autor} vivió {tiempoVivo.days} días")
    
    calcularDiasvivo.short_description = "Calcular días vividos" # Definimos el nombre q mostrara en los actions

    actions = [calcularDiasvivo] # agregamos las actions a la clase admin

    

# Registramos el modelo AutorBD con la configuración de AutorAdmin
admin.site.register(AutorBD, AutorAdmin)

@admin.register(FraseDB) ## Froma mas corta de registrar un modelo
class FraseAdmin(admin.ModelAdmin):
    fields = ["cita", "autor_fk"]
    list_display = ["cita", "autor_fk"]

