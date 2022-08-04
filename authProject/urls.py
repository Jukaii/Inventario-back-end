from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from authApp import views

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('categorias/', views.CategoriasView.as_view()),
    path('categorias/<int:pk>/', views.CategoriaDetail.as_view()),
    path('productos/', views.ProductosView.as_view()),
    path('productos/<int:pk>/', views.ProductosDetail.as_view()),
    path('rol/', views.RolView.as_view()),
    path('rol/<int:pk>/', views.RolDetail.as_view()),
]   