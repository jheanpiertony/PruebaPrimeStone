# PruebaPrimeStone
 PruebaPrimeStone

Eder Ortega Cardona

# Requerimientos
Python (3.7+)
```
pip install requirements.txt
```

# Estructura de proyecto
### common
* Modelo
* Api

### Front
* CRUD

# Api urls
### Obtener token
|Url| /api/token/|
|Method| POST |
|Json| ```{ "username": "admin", "password": "admin@1234" } ```|

### Api estudiantes
#### Crear
|Url| /common/student/|
|Method| POST |
|Json| ```{
    "name": "Diana",
    "last_name": "Restrepo",
    "birthdate": "1998-01-05",
    "gender": "F"
}```|
|Authorization| JWT <token> |

#### Actualizar
|Url| /common/student/<int:pk>|
|Method| PUT |
|Json| ```{
    "name": "Diana",
    "last_name": "Restrepo",
    "birthdate": "1998-01-05",
    "gender": "F"
}```|
|Authorization| JWT <token> |

#### Borrar
|Url| /common/student/<int:pk>|
|Method| DELETE |
|Json| |
|Authorization| JWT <token> |

# Configuración del logg

Actuializar la ruta del archivo del logg en settings.py

# Base de datos
SQLite: db.sqlite3
|Usuario| Contraseña|
|admin| admin@1234 |

De ser necesario actualice la configuración en settings.py a su base de datos.