from django.urls import path
from barbearia_alura.views import *

urlpatterns = [
    path('', index, name='index'),
    path('produtos/', produtos, name='produtos'),
    path('contato/', contato, name='contato')
]