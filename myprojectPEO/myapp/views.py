from django.shortcuts import render, redirect
from .models import Profesor, Estudiante, SistemaWeb, Cargo
from django.contrib import messages


def calificaciones(request):
    return render(request, 'calificaiones.html')

def CienciasNaturales(request):
    return render(request, 'CienciasNaturales.html')

def Cursos(request):
    return render(request, 'Cursos.html')

def Docentes(request):
    return render(request, 'Docentes.html')

def Eca(request):
    return render(request, 'Eca.html')

def Estudiantes(request):
    return render(request, 'Estudiantes.html')

def EstudiosSociales(request):
    return render(request, 'EstudiosSociales.html')

def Ingles(request):
    return render(request, 'Ingles.html')

def Items(request):
    return render(request, 'Items.html')

def LenguayLiteratura(request):
    return render(request, 'LenguayLiteratura.html')

def login(request):
    if request.method == 'POST':
        correoelectronico = request.POST.get('correoelectronico')
        cedula = request.POST.get('cedula')

        # Check if the user is a professor
        if Profesor.objects.filter(correoelectronico=correoelectronico, cedula=cedula).exists():
            return redirect('Docentes')
        # Check if the user is a student
        elif Estudiante.objects.filter(correoelectronico=correoelectronico, cedula=cedula).exists():
            return redirect('Estudiantes')

    return render(request, 'Login.html')

def Matematica(request):
    return render(request, 'Matematicas.html')

def Registro(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        cedula = request.POST['cedula']
        correoelectronico = request.POST['correoelectronico']
        cargo = request.POST['cargo']

        if cargo == 'docente':
            # Registro de docente
            Profesor.objects.create(
                nombre=nombre,
                apellido=apellido,
                cedula=cedula,
                correoelectronico=correoelectronico,
                # ... otros campos según sea necesario
                tipo_usuario='docente'
            )
        elif cargo == 'estudiante':
            # Registro de estudiante
            Estudiante.objects.create(
                nombre=nombre,
                apellido=apellido,
                cedula=cedula,
                correoelectronico=correoelectronico,
                # ... otros campos según sea necesario
                tipo_usuario='estudiante'
            )

        messages.success(request, '¡Registro exitoso! Inicia sesión con tus credenciales.')
        return redirect('Login')

    return render(request, 'Registro.html')

def calificaciones(request):
    return render(request, 'calificaciones.html')

def actividades(request):
    return render(request, 'actividades.html')





