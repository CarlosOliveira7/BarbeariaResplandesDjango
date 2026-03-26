from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClienteListView.as_view(), name='cliente_list'),
    path('novo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('editar/<int:pk>/', views.ClienteUpdateView.as_view(), name='cliente_update'),
    path('excluir/<int:pk>/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
]