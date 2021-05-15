"""
ESTE ARCHIVO SE CREA DENTRO DE UNA APLICACION PARA CREAR SUB-URLS
COMO EJEMPLO 127.0.0.1:8000/numero/uno  y 127.0.0.1:8000/numero/dos
"""

from django.urls import path
from aplicaciones.erp.views.category.views import *

# con [app_name] puedo darle una definicion mas especifica a los nombres de las url
# para diferenciar de que aplicacion viene ese nombre de url dentro de mi html poniendo un ejemplo --> 'erp:vista1'
app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_create'),
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/form/', CategoryFormView.as_view(), name='category_form'),
]
