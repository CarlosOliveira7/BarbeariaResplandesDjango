from django.urls import path
from . import views

urlpatterns = [
    path('', views.FinanceiroListView.as_view(), name='financeiro_list'),
    path('novo/', views.FinanceiroCreateView.as_view(), name='financeiro_create'),
    path('editar/<int:pk>/', views.FinanceiroUpdateView.as_view(), name='financeiro_update'),
    path('excluir/<int:pk>/', views.FinanceiroDeleteView.as_view(), name='financeiro_delete'),
]