from django import forms
from django.db import models
from django.forms.models import fields_for_model
from .models import Empleados
from django.forms import ModelForm, ClearableFileInput, widgets

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class ConsultaEmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = ['nombre','apellido','area','cargo']
        widgets = {
            'imagen': CustomClearableFileInput
        }