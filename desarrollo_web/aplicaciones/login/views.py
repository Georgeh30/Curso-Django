from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


# Create your views here.
class LoginFormView(LoginView):
    template_name = 'login.html'

    # Vamos a validar si ya tenemos nuestro inicio de sesion en nuestro sistema
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # Sí el usuario se encuentra con sesion activa
            return redirect('erp:category_list')  # Se redireccionara a la pagina list y si no ira al login
            print(request.user)  # Imprimimos esta variable para saber si nuestro usuario esta en sesion activa
        return super().dispatch(request, *args, **kwargs)

    # Metodo para poder enviar mas datos a mi template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context
