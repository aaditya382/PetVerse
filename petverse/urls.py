from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pets/', views.pets, name='pets'),
    path('shop/', views.shop, name='shop'),
    path('appointments/', views.appointments, name='appointments'),
    path('medicines/', views.medicines, name='medicines'),
    path('adoption/', views.adoption, name='adoption'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
]