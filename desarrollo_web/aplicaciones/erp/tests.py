import random

from django.test import TestCase
from config.wsgi import *
from aplicaciones.erp.models import *
# from aplicaciones.erp.models import Type, Employee

# Registro para guardar en la tabla Category
data = ['Leche y derivados', 'Carnes, pescados y huevos', 'Patatas, legumbres, frutos secos',
        'Verduras y Hortalizas', 'Frutas', 'Cereales y derivados, azúcar y dulces',
        'Grasas, aceite y mantequilla']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']

# OPCON 1 pocos registros, Interando para agregar los registros dentro de la tabla Category
# for i in data:
#     cat = Category(name=i)
#     cat.save()
#     print('Guardado registro N°{}'.format(cat.id))

# OPCION 2 muchos registros, Interando para agregar los registros dentro de la tabla Category
for i in range(1, 6000):
        name = ''.join(random.choices(letters, k=5))
        while Category.objects.filter(name=name).exists():
                name = ''.join(random.choices(letters, k=5))
        Category(name=name).save()
        print('Guardado registro {}'.format(i))

# A PARTIR DE AQUI son pruebas de como hacer consultas como: [listar, agregar, editar y eliminar] sin usar codigo de BD

""" ---------------------------------- Listar ----------------------------------------------- """
# query = Type.objects.all()  # Es como si hiciere una consulta asi --> select * from Type;
# print(query)

""" --------------------------------- Insercion ---------------------------------------------- """
# OPCION 1
# Type(name='Prueba_opc1').save()  # INSERT INTO Type (name) VALUES ('Prueba_opc1');

# OPCION 2
# t = Type()
# t.name = 'Prueba_opc2'
# t.save()

""" --------------------------------- Editar ---------------------------------------------------- """
# try:
#     t1 = Employee.objects.get(id=1)  # Hacemos una Consulta para obtener un solo regitro que tenga id o pk 1
#     t1.names = 'George'  # Y le indicamos que lo modifique por George
#     t1.save()  # Y confirmamos que guarde el cambio en la tabla correspondiente
# except Exception as e:
#     print(e)
#
# print(t1.dni)
# print(t1.names)

""" ---------------------------------- Eliminar -------------------------------------------------- """
# try:
#     t = Type.objects.get(pk=2)  # Buscamos el registro con el id ó el pk 2
#     t.delete()  # Y confirmamos la eliminacion del registro
# except Exception as e:
#     print(e)


"""
 Las que comiencen con la letras [Mi]
"""
# for i in Type.objects.filter(name__startswith='Mi'):  # SELECT * FROM Type WHERE name LIKE 'Mi%';
#     print(i.name)

"""
Busca los nombres que contengan [Mi] respetando MAYUSCULAS y minusculas con el comando [nombredelacolumna__contains]
y para no respetarlas seria con [nombredelacolumna__icontains]
"""
# obj = Type.objects.filter(name__contains='ll')  # SELECT * FROM Type WHERE name LIKE '%ll%';
# objq = Type.objects.filter(name__contains='ll').query  # Muestra la consulta en formato de comando de una Base de Datos

"""
Excluye el id ó pk 2 al buscar todos los que comiencen con [Mi]
"""
# SELECT "id", "name" FROM "tipo" WHERE ("name"::text LIKE %a AND NOT ("id" = 4)) ORDER BY "id" ASC
# obj22 = Type.objects.filter(name__startswith='Mi').exclude(id=3)

"""
Las que terminen con la [a]
"""
# obj2 = Type.objects.filter(name__endswith='a')  # SELECT * FROM Type WHERE name LIKE '%a';

"""
Buscar varios registros que sean iguales a [Definis] y [Controu] a la vez respetando MAYUSCULAS y minusculas
y mostrará las palabras cuantas veces las encuentre, PERO!! igual podemos regresar el numero de registro
que encontro con --> .count()
"""
# obj3 = Type.objects.filter(name__in=['Definis', 'Controu']).count()

# print(objq)
# print(str(obj) + '\n' + str(obj2) + '\n' + str(obj3))
# print(obj22)
