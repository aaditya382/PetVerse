from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.pets, name='pets'),
    path('shop/', views.shop, name='shop'),
   path('appointment/', views.appointments, name='appointments'),
    path('medicines/', views.medicines, name='medicines'),
    path('adoption/', views.adoption, name='adoption'),
    path('login/', views.login, name='login'),
]