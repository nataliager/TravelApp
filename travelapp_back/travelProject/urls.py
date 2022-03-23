from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from travelApp import views
from django.contrib import admin

urlpatterns = [

    #URL administrador
    path('admin/', admin.site.urls), #panel de administrador

    #URLs login
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    #URLs modelo User
    path('user', views.UserCreateView.as_view()),#crear un usuario
    #valor entero con el ID pk
    path('user-view/', views.UserView.as_view()),#obtener y actualizar datos del usuario

    #URLs modelo Flight
    path('flightCreate', views.FlightCreateView.as_view()), #Agregar un vuelo a la BD
    path('flightDetail', views.FlightApiView.as_view()),#Obtiene todos los vuelos de la BD
    path('flight/<str:pk>/', views.FlightDetailView.as_view()),#GET,PUT,DELETE de la BD segun pk

    #URLs modelo Booking
    path('booking', views.BookingView.as_view()), #Crear reserva
    path('booking/<int:pk>/', views.BookingView.as_view()) #Obtener y eliminar una reserva por la PK


]

