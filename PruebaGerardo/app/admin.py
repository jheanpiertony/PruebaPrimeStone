from django.contrib import admin
from api.models import Curso, Estudiante, Direccion

""" 
Creditos

Autor = Gerardo Beltran Pulido
version = "1.0.0
correo = "gerbel06@gmail.com
Estado = "Dev
Fecha = "2021-06-04


"""

"""Se registran los modelos a usar dentro del admin de django"""

admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Direccion)
