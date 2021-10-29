from django.urls import path
from .views import listaEstadios

urlpatterns = [
    path('', listaEstadios, name='listaEstadios'),
]