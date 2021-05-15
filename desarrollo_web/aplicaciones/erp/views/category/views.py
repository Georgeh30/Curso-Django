from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView

from aplicaciones.erp.forms import CategoryForm
from aplicaciones.erp.models import Category
from django.utils.decorators import method_decorator  # Permite agregarle una funcion decoradora a otra

# Validar si el usuario esta logeado antes de entrar antes de entrar a la pagina que solicita
from django.contrib.auth.decorators import login_required


# Clase para listar los registros de la tabla Category
class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    # Sobreescritura del Metodo dispatch para redireccionar con el GET o POST y...
    # el method_decorator para agregar a la funcion la validacion de login
    # @method_decorator(login_required)  # Valida que este logeado
    @method_decorator(csrf_exempt)  # Indicamos que no le de seguridad de token al metodo de mas abajo POST
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # Sobreescritura del Metodo POST parte de Django
    def post(self, request, *args, **kwargs):
        data = {}  # Inicializamos variable, que NO es parte de las variables por default de Django
        try:
            # Indicamos que busque el registro con el id obtenido de la funcion Ajax y lo guarde en la variable "data"
            # data = Category.objects.get(pk=request.POST['id']).toJSON()
            # data['name'] = cat.name

            action = request.POST['action']  # Obtenemos mediante el post el contenido de la variable [action]
            if action == 'searchdata':  # si el contenido de [action] es igual a [searchdata] entonces...
                data = []  # Creamos e inicializamos una variable
                for i in Category.objects.all():  # Realizamos una interacion para obtener todos los registro
                    data.append(i.toJSON())  # Y los convertimos a tipo JSON y los guardamos en la variable [data]
            else:  # Si el contenido de la variable [action] NO es igual a [searchdata] entonces...
                data['error'] = 'Ha ocurrido un Error'  # Guardara un mensaje ['error': 'Ha ocurrido un Error']
        except Exception as e:
            # Si hubo un error guardar la exception en la variable "data"
            data['error'] = str(e)
        # Lo enviamos en Formato Json que se puede ver en Console de la Pagina Web
        return JsonResponse(data, safe=False)  # Podemos enviar mas de un registro con [safe=False]

    # Metodo de las vistas basadas en clase sobreescrita para enviar mas de una variable al html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        context['create_url'] = reverse_lazy('erp:category_create')  # Para darle la url al boton [Nuevo Registro]
        context['list_url'] = reverse_lazy('erp:category_list')  # Para darle la url al boton [Categorías]
        context['entity'] = 'Categorías'
        return context


# Clase para crear un nuevo registro dentro de la tabla Category
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm  # Envia el form al html que esta dentro de la variable [template_name]
    template_name = 'category/create.html'  # Ingresa con metodo GET
    # ESTE success_url ES PARTE DE LA PRIMERA FORMA DE ENVIAR LOS DATOS DEL FORM A TRAVES DE POST USANDO DJANGO
    success_url = reverse_lazy('erp:category_list')  # Redirecciona con metodo POST

    # Sobreescritura del Metodo POST parte de Django,
    # pero usada para obtener los datos siendo llamado detro de la funcion AJAX
    def post(self, request, *args, **kwargs):
        data = {}  # Inicializamos variable, que NO es parte de las variables por default de Django
        try:
            action = request.POST['action']  # Recupero esta variable y su contenido del form.html
            if action == 'add':
                # form = self.get_form()  # Hace lo mismo que la linea de abajo solo que este no podria guardar img
                form = CategoryForm(request.POST)  # Obtenemos el formulario pasandole los campos mediande POST
                data = form.save()  # que guarde los [errores ó los datos validos] dentro de la variable [data]
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            # Si hubo un error guardar la exception en la variable "data"
            data['error'] = str(e)
        return JsonResponse(data)  # Lo enviamos en Formato Json que se puede ver en Console de la Pagina Web

    # Metodo de las vistas basadas en clase sobreescrita para enviar mas de una variable al html
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una Categoria'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('erp:category_list')  # Para darle la url al boton [Categorías]
        # ESTA VARIABLE SE ENVIA AL form.html Y SÍ ENTRA AL CAMPO DONDE SE LA PUSIMO, ENTONCES
        # LA PODEMOS OBTENER DENTRO DEL METODO POST DE ARRIBA
        context['action'] = 'add'
        return context


# Clase para actualizar un registro dentro de la tabla Category
class CategoryUpdateView(UpdateView):
    model = Category  # Obtiene el registro con id que obtuvimos a traves de la url
    form_class = CategoryForm  # Envia el form al html que esta dentro de la variable [template_name] de abajo, ya con los campos llenos
    template_name = 'category/create.html'  # Ingresa con metodo GET
    # ESTE success_url ES PARTE DE LA PRIMERA FORMA DE ENVIAR LOS DATOS DEL FORM A TRAVES DE POST USANDO DJANGO
    success_url = reverse_lazy('erp:category_list')  # Redirecciona con metodo POST

    # MODIFICAMOS ESTE METODO PARA QUE EL METODO POST DE ABAJO PUEDA GUARDAR EL UPDATE DEL REGISTRO, DICIENDOLE
    # AL self.object EL CUAL ES DONDE AUN NO SE A UPDATE EL REGISTRO, QUE GUARDE DENTRO DE ÉL EL CAMBIO O
    # UPDATE QUE YA ESTA GUARDADO DENTRO DE self.get_object() Y ASI SE VEA REFLEJADO EL UPDATE
    def dispatch(self, request, *args, **kwargs):
        # Le decimos al "object" que va a ser igual a lo que hay en la instancia del objeto para
        # que no se altere el funcionamiento de la clase update y el metodo de abajo post pueda guardar la modificacion
        # del registro
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    # Sobreescritura del Metodo POST parte de Django,
    # pero usada para obtener los datos y guardar en la tabla, siendo llamado detro de la funcion AJAX
    def post(self, request, *args, **kwargs):
        data = {}  # Inicializamos variable, que NO es parte de las variables por default de Django
        try:
            action = request.POST['action']  # Recupero esta variable y su contenido del form.html
            if action == 'edit':
                # NOTA: EL self.form() SÍ FUNCIONA EN ESTA CLASE PERO EL CategoryForm(request.POST) NO HACE EL UPDATE
                form = self.get_form()  # Hace lo mismo que la linea de abajo solo que este no podria guardar img
                # form = CategoryForm(request.POST)  # Obtenemos el formulario pasandole los campos mediande POST
                data = form.save()  # que guarde [los errores o los datos] dentro de la variable [data]
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            # Si hubo un error guardar la exception en la variable "data"
            data['error'] = str(e)
        return JsonResponse(data)  # Lo enviamos en Formato Json que se puede ver en Console de la Pagina Web

    # Metodo de las vistas basadas en clase sobreescrita para enviar mas de una variable al html
    def get_context_data(self, **kwargs):
        # print(self.object)
        # print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de una Categoria'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('erp:category_list')  # Para darle la url al boton [Categorías]
        # ESTA VARIABLE SE ENVIA AL form.html Y SÍ ENTRA AL CAMPO DONDE SE LA PUSIMO, ENTONCES
        # LA PODEMOS OBTENER DENTRO DEL METODO POST DE ARRIBA
        context['action'] = 'edit'
        return context


# Clase para eliminar un registro dentro de la tabla Category
class CategoryDeleteView(DeleteView):
    model = Category  # Obtiene el registro con id que obtuvimos a traves de la url
    template_name = 'category/delete.html'  # Ingresa con metodo GET
    # ESTE success_url ES PARTE DE LA PRIMERA FORMA DE ENVIAR LOS DATOS DEL FORM A TRAVES DE POST USANDO DJANGO
    success_url = reverse_lazy('erp:category_list')  # Redirecciona con metodo POST

    def dispatch(self, request, *args, **kwargs):
        # Le decimos al "object" que va a ser igual a lo que hay en la instancia del objeto para
        # que no se altere el funcionamiento de la clase update y el metodo de abajo post pueda guardar la modificacion
        # del registro
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    # Metodo de las vistas basadas en clase sobreescrita para enviar mas de una variable al html
    def get_context_data(self, **kwargs):
        # print(self.object)
        # print(self.get_object())
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de una Categoria'
        context['entity'] = 'Categorías'
        context['list_url'] = reverse_lazy('erp:category_list')  # Para darle la url al boton [Categorías]
        return context


# Esta clase nos servira para la parte del login
# Clase que al igual que las otras clases servira para validar si el form es valido y por ende retornara hacia
# una url de exito
class CategoryFormView(FormView):
    form_class = CategoryForm  # Formulario con el que va a trabajar
    template_name = 'category/create.html'  # EL template (EL HTML) con el que va a trabajar (a ingresar en GET)
    success_url = reverse_lazy('erp:category_list')  # Le indicamos que retorne hacia el listado cuando sea POST el HTML

    # Cuando el form es valido, trabajamos con este metodo
    def form_valid(self, form):
        print(form.is_valid())
        print(form)
        return super().form_valid(form)

    # Para ver el error del form, trabajamos con este metodo
    def form_invalid(self, form):
        print(form.is_valid())  # Imprime un bool, False ó True, sí el form es valido o no
        print(form.errors)  # Imprime el error
        return super().form_invalid(form)  # Que retorne lo mismo para no afectar en nada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Llamo primero a la implementación base para obtener un contexto
        # Para poder agregar mas datos dentro del diccionario "context"
        context['title'] = 'Form | Categoria'
        context['entity'] = 'Categoria'
        context['list_url'] = reverse_lazy('erp:category_list')
        context['action'] = 'add'
        return context
