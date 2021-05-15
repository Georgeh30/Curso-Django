"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from aplicaciones.homepage.views import IndexView
from aplicaciones.login.views import LoginFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('erp/', include('aplicaciones.erp.urls')),  # URL Para ingresar a las sub-url de la aplicacion [erp]

    # Son vistas de dos aplicaciones donde solo se hace una sola cosa por eso las ponemos directas en el urls principal
    path('', IndexView.as_view(), name='index'),  # Para acceder al Inicio de la Pagina Web
    path('login/', LoginFormView.as_view(), name='login'),  # Para acceder a la Pantalla de Logueo
]
