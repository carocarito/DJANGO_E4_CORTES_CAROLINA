from django import forms
from appReservas.models import Reserva
from django.core import validators

class NuevaReserva(forms.ModelForm):
    class Meta:
        model = Reserva
        fields= '__all__'
        ESTADOS = [('reservado', 'RESERVADO'),('completado', 'COMPLETADO'),('anulada','ANULADA'),('no asisten', 'NO ASISTEN')]
        def clean_cliente(self):
            inputCliente = self.cleaned_data['cliente']
            if inputCliente == False:
                raise forms.ValidationError("El campo no puede estar vacío")
            return inputCliente
        def clean_fono(self):
            inputFono = self.cleaned_data['fono']
            if inputFono == False:
                raise forms.ValidationError("El campo no puede estar vacío")
            return inputFono
        def clean_fecha(self):
            inputFecha = self.cleaned_data['fecha']
            if inputFecha == False:
                raise forms.ValidationError("El campo no puede estar vacío")
            return inputFecha
        def clean_hora(self):
            inputHora = self.cleaned_data['fono']
            if inputHora == False:
                raise forms.ValidationError("El campo no puede estar vacío")
            return inputHora
        def clean_comensales(self):
            inputComensales = self.cleaned_data['comensales']
            if (inputComensales < 1 | inputComensales > 15):
                raise forms.ValidationError("comensales debe estar entre 1 y 15")
            return inputComensales
        estado = forms.CharField(widget=forms.Select(choices=ESTADOS))
        
        
