from django.urls import path
from . import views

urlpatterns = [
    #URL vazia  direciona para a view lista_tarefas
    path('',views.lista_tarefas, name='home'),
    path('concluir/<int:tarefa_id>/', views.concluir_tarefa, name='concluir'),
    ]
path('deletar/<int:tarefa_id>/', views.deletar_tarefa, name='deletar'),
