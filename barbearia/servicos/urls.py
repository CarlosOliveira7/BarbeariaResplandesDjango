from django.urls import path
from . import views

urlpatterns = [
    path('', views.ServicoListView.as_view(), name='listar_servicos'),
    path('novo/', views.ServicoCreateView.as_view(), name='servico_create'),
    path('editar/<int:pk>/', views.ServicoUpdateView.as_view(), name='servico_update'),
    path('excluir/<int:pk>/', views.ServicoDeleteView.as_view(), name='servico_delete'),
]