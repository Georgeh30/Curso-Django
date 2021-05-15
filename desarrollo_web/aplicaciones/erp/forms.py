from django.forms import *

from aplicaciones.erp.models import Category


class CategoryForm(ModelForm):

    """ OPCION 1 PARA PONER ATRIBUTOS HTML DJANGO O PARA QUE NO SE REPITAN EN LA OPCION 2 DE ABAJO """
    # Este metodo nos ayuda a modificar o agregar un estilo mas a cada campo sin necesitdad de ir al html
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Iteramos dentro de cada campo del formulario para asignarle atributos que se repitan en todos los campos
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'  # [class] es uno de los atributos de las etiquetas de html de estilo css
            form.field.widget.attrs['autocomplete'] = 'off'

        # Aqui sí especifico a cual campo quiero agregarle un estilo o atributos mas.
        self.fields['name'].widget.attrs['autofocus'] = True  # Para que este resaltado este campo al iniciar la pagina

    class Meta:
        model = Category
        fields = '__all__'

        # Sirve para cambiar el nombre del label de cada campo de la tabla que se mostrara en el formulario,
        # aunque no es necesario ya que en las tablas o modelos tiene [verbose_name] para dar el nombre al label
        # labels = {
        #     'desc': 'Descripción',
        #     'name': 'Nombre',
        # }

        """ OPCION 2 PARA AGREGAR ATRIBUTOS HTML CON DJANGO A CADA CAMPO """
        # Funciona para que dentro de él se pueda modificar el estilo a cada campo de la tabla
        # indicando como clave el nombre del campo puesto en la tabla o modelo
        widgets = {
            'name': TextInput(
                # El [attrs] sirve para agregar los atributos que le faltan para darle un mejor estilo al objeto
                attrs={
                    # 'class': 'form-control',  # [class] es uno de los atributos de las etiquetas de html de estilo css
                    'placeholder': 'Ingresa un Nombre',
                    # 'autocomplete': 'off'
                }
            ),
            'desc': Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingresa una Descripción',
                    # 'autocomplete': 'off',
                    'rows': 3,
                    'cols': 3,
                }
            ),
        }

    # Sobreescritura del metodo save, usada para agregar al modelo o tabla los datos enviados a traves de ajax
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():  # si el formulario esta bien
                form.save()  # entonces lo guardaremos para poder registrarlos datos de los campos del formulario dentro de list
            else:  # y si no es correcto el formulario
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

    # Ver como funciona los errores que mostramos en form.html hasta abajo dentro de las etiquetas javascript
    def clean(self):
        cleaned = super().clean()  # Obtenemos el objeto de nuestro formulario
        # Para ver como funcionan los errores, pero igualmente nos sirve para hacer validaciones dentro de formulario
        if len(cleaned['name']) <= 50:  # Si la longitud es menor a 50 caracteries
            # Este es otro tipo de errores que controlamos con form.non_field_errors
            raise forms.ValidationError('Validacion del error')
            # self.add_error('name', 'Le faltan caracteres')
        return cleaned
