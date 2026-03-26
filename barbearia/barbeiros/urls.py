from django.urls import path
from . import views

urlpatterns = [
    path('', views.BarbeiroListView.as_view(), name='barbeiro_list'),
    path('barbeiros/novo/', views.BarbeiroCreateView.as_view(), name='barbeiro_create'),
    path('barbeiros/editar/<int:pk>/', views.BarbeiroUpdateView.as_view(), name='barbeiro_update'),
    path('barbeiros/excluir/<int:pk>/', views.BarbeiroDeleteView.as_view(), name='barbeiro_delete'),
]