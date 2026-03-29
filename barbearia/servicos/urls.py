from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServicoListView.as_view(), name='listar_servicos'),
    path('novo', views.ServicoCreateView.as_view(), name='cadastrar_servico'),
]