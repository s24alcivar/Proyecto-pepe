from django.urls import path
from . import views 

urlpatterns = [
    path ('Login/', views.login, name='Login'),
    path ('Registro/', views.Registro, name='Registro'),
    path ('Items/', views.Items, name='Items'),
    path ('Cursos/', views.Cursos, name='Cursos'),
    path('Eca/', views.Eca, name='Eca'),
    path ('EstudiosSociales/', views.EstudiosSociales, name='EstudiosSociales'),
    path ('CienciasNaturales/', views.CienciasNaturales, name='CienciasNaturales'),
    path ('Ingles/', views.Ingles, name='Ingles'),
    path ('Matematica/', views.Matematica, name='Matematica'),
    path ('Docentes/', views.Docentes, name='Docentes'),
    path ('Estudiantes/', views.Estudiantes, name='Estudiantes'),
    path ('calificaciones/', views.calificaciones, name='calificaciones'),
    path ('LenguayLiteratura/', views.LenguayLiteratura, name='LenguayLiteratura'),
    path ('actividades/', views.actividades, name='actividades'),
    # Add your other URL patterns here
]