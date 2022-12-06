from django.shortcuts import render, redirect
from appReservas.models import *
from appReservas.forms import *

# Create your views here.
def index(request):
    return render(request, 'templatesApp/index.html')

def listaReservas(request):
    reservas = Reserva.objects.all()
    data={'reservas': reservas}
    return render(request, 'templatesApp/listaReservas.html',data)


def agregarReserva(request):
    form = NuevaReserva()
    if request.method == 'POST':
        form = NuevaReserva(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data={'form':form}
    return render (request,'templatesApp/nuevaReserva.html',data)

def eliminarReserva(request,id):
    reservas = Reserva.objects.get(id=id)
    reservas.delete()
    return redirect('/listaReservas')

def actualizarReserva(request,id):
    reservas=Reserva.objects.get(id=id)
    form= NuevaReserva(instance=Reserva)
    if(request.method=='POST'):
        form=NuevaReserva(request.POST, instance=reservas)
        if(form.is_valid()):
            form.save()
            return redirect('/listaReservas')
    data = {'form':form,'TITULO':'ACTUALIZAR RESERVA'}
    return render (request,'templatesApp/agregarReserva.html',data)
