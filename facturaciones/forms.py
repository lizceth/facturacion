from django import forms
"""
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Button, Submit, Fieldset, HTML, Field
from crispy_forms.bootstrap import FormActions
"""
from .models import Cliente, Factura, Producto, Detalle
from django.forms import ModelForm

class ClienteForm(ModelForm):
    class Meta:
        model=Cliente

class ProductoForm(ModelForm):
     class Meta:
         model = Producto

class FacturaForm(ModelForm):
     class Meta:
         model = Factura

class DetalleForm(ModelForm):
     class Meta:
         model = Detalle
