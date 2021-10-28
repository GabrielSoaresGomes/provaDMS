from django.urls import path, include
from .views import listaEstadios, adicionarEstadio, atualizarEstadio, deletarEstadio, escolherEstadio

urlpatterns = [
    path('', listaEstadios, name='listaEstadios'),
    path('novo', adicionarEstadio, name="adicionarEstadio"),
    path('atualizar/<int:id>', atualizarEstadio, name="atualizarEstadio"),
    path('deletar/<int:id>', deletarEstadio, name="deletarEstadio"),
    path('escolher/<int:id>', escolherEstadio, name="escolherEstadio"),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls'), name='members'),
]