from django.urls import path
from . import views

urlpatterns = [
    path('', views.AgendamentoListView.as_view(), name='agendamento_list'),
    path('novo/', views.AgendamentoCreateView.as_view(), name='agendamento_create'),
    path('editar/<int:pk>/', views.AgendamentoUpdateView.as_view(), name='agendamento_update'),
    path('excluir/<int:pk>/', views.AgendamentoDeleteView.as_view(), name='agendamento_delete'),
]