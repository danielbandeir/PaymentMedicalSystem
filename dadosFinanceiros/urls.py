from django.urls import path
from .views import createPagamento, searchPagamento, delPagamento, editPagamento


urlpatterns = [
    path('adicionar/', createPagamento, name="criarPagamento"),
    path('buscar/', searchPagamento, name="buscarPagamento"),
    path('deletar/<int:pk>', delPagamento, name="deletarPagamento"),
    path('editar/<int:pk>', editPagamento, name="editarPagamento"),
]
