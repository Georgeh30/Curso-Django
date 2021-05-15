from django.db import models
from datetime import datetime

from django.forms import model_to_dict

from aplicaciones.erp.choices import gender_choices


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, verbose_name='Descripción', null=True, blank=True)

    def __str__(self):
        return self.name

    # Metodo NO es parte de Django, si no un metodo nuevo para enviar datos en formato json
    def toJSON(self):
        # [model_to_dict] convierte el/los registro/s obtenido/s en un diccionario, se puede excluir un/los registro/s
        # escribiendo despues del [self]  esto --> [, exclude={''}]
        item = model_to_dict(self)  # Este sirve para hacer lo mismo que el de la linea de abajo
        # item = {'id': self.id, 'name': self.name}
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categoria'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')

    # [upload_to] sirve para indicar la ruta donde guardara la imagen o archivo con el nombre de [product/aa/mm/dd]
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')
    surnames = models.CharField(max_length=150, verbose_name='Apellidos')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Dirección')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Sexo')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Cliente'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Cliente')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de Registro')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names  # Decimos que queremos obtener el nombre del cliente de la otra tabla Client

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Venta'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        db_table = 'Detalle de Venta'
        ordering = ['id']


""" ---------------------------------------- CLASES DE EJEMPLO -------------------------------------------------- """

# class Type(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Tipo'  # Damos nombre a la Tabla dentro del sitio de administracion django
#         verbose_name_plural = 'Tipos'  # Damos nombre a la Tabla dentro del sitio de administracion django
#         db_table = 'tipo'  # Damos un Nombre a la Tabla
#         ordering = ['id']  # Ordena de manera ascendente y con -id de manera descendente
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=150, verbose_name='Nombre')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Categoria'  # Damos nombre a la Tabla dentro del sitio de administracion django
#         verbose_name_plural = 'Categorias'  # Damos nombre a la Tabla dentro del sitio de administracion django
#         db_table = 'categoria'  # Damos un Nombre a la Tabla
#         ordering = ['id']  # Ordena de manera ascendente y con -id de manera descendente
#
#
# class Employee(models.Model):
#     # Al poner [ManyToManyField] dentro de la BD creará una tabla extra de relacion entre "Category" y "Employee"
#     categ = models.ManyToManyField(Category, verbose_name='Categoria')  # Llave foranea de tabla category
#     type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name='Tipo')  # Llave foranea de tabla type
#     names = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
#     dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
#     date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')
#     date_creation = models.DateField(auto_now=True, verbose_name='Fecha de creacion')
#     date_updated = models.DateTimeField(auto_now_add=True, verbose_name='Fecha actualizada')
#     age = models.PositiveIntegerField(default=0, verbose_name='Años')
#     salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Salario')
#     state = models.BooleanField(default=True, verbose_name='Estado')
#
#     # null y blank para que dentro de cada uno este vacio por defecto
#     avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', verbose_name='Foto', null=True, blank=True)
#     cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', verbose_name='Curriculum', null=True, blank=True)
#
#     def __str__(self):
#         return self.names  # Para que muestre la lista de los registro por nombre dentro del sitio admin de django
#
#     class Meta:
#         verbose_name = 'Empleado'  # Damos nombre a la Tabla dentro del sitio de administracion django
#         verbose_name_plural = 'Empleados'  # Damos nombre a la Tabla dentro del sitio de administracion django
#         db_table = 'empleado'  # Damos un Nombre a la Tabla
#         ordering = ['id']  # Ordena de manera ascendente y con -id de manera descendente
