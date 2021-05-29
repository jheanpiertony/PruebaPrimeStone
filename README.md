# PruebaPrimeStone
 PruebaPrimeStone


proyecto creado para prueba tecnica solicitada por la empresa PRIMESTONE.

## Instalacion

Aplicacion hecha en python-django cuenta con el archivo requirements.txt el cual se corre en el entorno virtual activo, una vez instaladas las libreria se puede proceder a correr el proyecto

```bash
VIRTUALENV
> pip install -r requirements.txt
> python manage.py runserver
```

## Estructura
La aplicacion fue hecha en python con el framework Django, las api fueron hechas ocn la libreria proporcionada por django(djangorestframework)
Inicialmente tenemos la carpeta principal llamada SchoolAdmin
la cual contiene la carpeta logs que guarda los errores ocurridos en la api
-static la cual contiene todos los assets de la plantilla
-templates la cual contiene los html correspondientes al programa
-SchoolAdmin carpeta donde se encuentra toda la configuracion del proyecto y las rutas del mismo
-school_app carpeta donde se encuentran los metodos, vistas, modelos, api y funciones usada por la aplicacion

## Puntos solicitados
-ORM para este proyecto se uso el ORM propio de django el cual crea las tablas con el comando python manage.py migrate y python manage.py makemigrations
-CRUD DIRECCION SP en la raiz de proyecto encontraran el script correspondiente a la base de datos la cual tiene los SP usados
-DoWork en el archivo principal de la app (views.py) se encuentra la funcion llamada doWork la cual usa un threading.Timer de 10 segundos que guarda en el modelo DoWork
-API REST con JWT se encuentran en el archivo api.py y las url y parametros son explicados en este mismo documento mas abajo
-Logs a base de archivo de texto para las API los cuales se guardan en la carpeta logs

## Uso
Una vez ejecutada la aplicacion cuenta con dos urls las cuales son:
```python
http://localhost:8000/admin/ #para acceder al admin proporcionado por django USUARIO:admin_school CONTRASEÑA:Prime*2021
http://localhost:8000/api_login/ #URL PARA LOGEO EL CUAL ARROJA EL TOKEN SOLICITADO POR LAS API DE ESTUDIANTE
#LAS SIGUIENTES API RECIBEN EL TOKEN EN EL HEADER DE PARAMETRO EJ:
# "key":"Authorization","value":"Token  93dc795d8038fd8984c4198ee664396bc2dff960"
http://localhost:8000/api_crear_estudiante/ #API PARA CREAR ESTUDIANTE
#RECIBE
# nombres
# apellidos
# fecha_nacimiento
# genero
http://localhost:8000/api_crear_editar_estudiantes/#API PARA CREAR O EDITAR ESTUDIANTE
#RECIBE
# id
# nombres
# apellidos
# fecha_nacimiento
# genero
http://localhost:8000/api_consultar_estudiantes/#API PARA CONSULTAR ESTUDIANTE
http://localhost:8000/api_eliminar_estudiantes/#API PARA ELIMINAR ESTUDIANTE
#RECIBE
# id
http://localhost:8000/api_datos_estudiantes/#API PARA CONSULTAR DATOS DE UN ESTUDIANTE
#RECIBE
# id
```

