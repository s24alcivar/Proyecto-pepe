from django.db import models

class Profesor(models.Model):
    idprofesores = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15)
    correoelectronico = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=20, default='docente')

    def _str_(self):
        return self.profesor
    
class Estudiante(models.Model):
    idestudiantes = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=15)
    correoelectronico = models.CharField(max_length=100)
    tipo_usuario = models.CharField(max_length=20, default='estudiante')

    def _str_(self):
        return self.estudiante
    
class SistemaWeb(models.Model):
    idsistemaweb = models.CharField(max_length=50)
    actividades = models.CharField(max_length=100)
    calificaciones = models.CharField(max_length=100)
    materias = models.CharField(max_length=15)
    
    def _str_(self):
        return self.sistemaweb
    
class Cargo(models.Model):
    idestudiantes = models.CharField(max_length=50)
    idprofesores = models.CharField(max_length=100)

    def _str_(self):
        return self.cargo
