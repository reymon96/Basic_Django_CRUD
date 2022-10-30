from ast import Try
from django.shortcuts import render, redirect
from . models import curso

# Create your views here.
def home(request):
    #extraer los datos de la base sqlite
    cursos = curso.objects.all()
    #retornarlos a la vista principal
    return render(request, 'gestionCursos.html', {"cursos":cursos})

def register(request):
    #recepcion de los datos enviados por el formulario
    codigo = request.POST['t_codigo']
    nombre = request.POST['t_nombre']
    creditos = request.POST['n_creditos']
    
    try:
        #Busquedo del Id en la BD
        find = curso.objects.get(codigo=codigo)
    except:
        #creacion del objeto para el registro en BD si el Id es unico
        curso.objects.create(codigo = codigo, nombre = nombre, creditos = creditos)
        return redirect('/')

def edit(request, codigo):
    ed_curso = curso.objects.get(codigo=codigo)
    return render(request, 'edicionCursos.html', {"curso":ed_curso})

def update(request):
    #recepcion de los datos enviados por el formulario
    ed_curso = curso.objects.get(codigo=request.POST['t_codigo'])
    nombre = request.POST['t_nombre']
    creditos = request.POST['n_creditos']
    ed_curso.nombre = nombre
    ed_curso.creditos = creditos
    ed_curso.save()
    return redirect('/')

def delete(request, codigo):
    #Eliminacion completa de la fila
    id_curso = curso.objects.get(codigo=codigo)
    id_curso.delete()
    return redirect('/')