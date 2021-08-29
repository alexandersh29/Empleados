from django.shortcuts import render
from .models import Empleados
from .models import *
from .forms import ConsultaEmpleadoForm
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def principal(request):
    empleados = Empleados.objects.all()
    return render(request, "registros/principal.html", {'empleados': empleados})


def consultarEmpleados(request):
    empleados = Empleados.objects.all()
    return render(request, "registros/consultaEmpleado.html", {'empleados': empleados})

def registrar(request):
    if request.method == 'POST':
        form = ConsultaEmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            empleados = Empleados.objects.all()
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            area = request.POST['area']
            cargo = request.POST['cargo']
            adicional = request.POST['adicional']
            imagen = request.FILES['imagen']
            insert = Empleados(nombre=nombre, apellido=apellido,area=area,cargo=cargo,adicional=adicional, imagen=imagen)
            insert.save()
            return render(request, "registros/consultaEmpleado.html", {'empleados': empleados})
        else:
            messages.error(request, "Error al procesar el formulario")
    form = ConsultaEmpleadoForm()
    return render(request, 'registros/crearEmpleado.html', {'form': form})



def eliminarEmpleado(request, id, confirmacion='registros/confirmarEliminacion.html'):
    empleado = get_object_or_404(Empleados, id=id)
    if request.method=='POST':
        empleado.delete()
        empleados=Empleados.objects.all()
        return render(request,"registros/consultaEmpleado.html", {'empleados':empleados})
        
    return render(request, confirmacion, {'object':empleado})

def consultarEmpleadoIndividual(request, id):
    empleado = Empleados.objects.get(id=id)
    return render(request, "registros/formEditarEmpleado.html", {'empleado': empleado})


def editarEmpleado(request, id):
    empleado = get_object_or_404(Empleados, id=id)
    form = ConsultaEmpleadoForm(request.POST,request.FILES, instance=empleado)
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        empleados=Empleados.objects.all()
        return render(request,"registros/consultaEmpleado.html", {'empleados':empleados})

    return render(request,"registros/formEditarEmpleado.html", {'empleado':empleado})