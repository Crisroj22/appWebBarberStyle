from django import forms
from intranet.models import Producto


class FormBodega(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'faltante' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'vendido' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'descuento' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            ),
            'valor_unitario' : forms.HiddenInput(
                attrs={
                    'required':False
                }
            )
        }
        

class FormBarbero(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'