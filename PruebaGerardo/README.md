# PruebaPrimeStone
 PruebaPrimeStone





# Requerimientos
Python (3.7)
```
pip install requirements.txt
```

#Front









# Api urls
### Obtener token
|Url| /api/token/|
|Method| POST |
|Json| ```{ "username": "admin", "password": "admin" } ```|

### Ejemplo obtener token



### Ejemplo consumo api sin token


### Ejemplo consumo api con token



### Api estudiantes
#### Crear
|Url| /api/student/|
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




