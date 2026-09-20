from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home, name='api_home'),
    path('contract/', views.contract_list, name='contract_list'),
    path('contract/<int:pk>/', views.contract_detail, name='contract_detail'),
]
