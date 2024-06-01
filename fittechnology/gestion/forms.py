from django import forms
from .models import Clasificacion, DatosPersona


class ClasificacionForm(forms.ModelForm):
    class Meta:
        model = Clasificacion
        fields = ['codigo', 'descripcion']
        widgets = {

            'codigo': forms.TextInput(attrs={'class': 'form-control'}),

            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Descripción',
                'onkeyup': "javascript:this.value=this.value.toUpperCase();",
            })
        }


class DatosPersonaForm(forms.ModelForm):
    class Meta:
        model = DatosPersona
        fields = ['tipo_identificacion', 'identificacion', 'primer_nombre', 'segundo_nombre', 'primer_apellido',
                  'segundo_apellido', 'fecha_nacimiento', 'sexo', 'peso', 'altura']
        widgets = {
            'tipo_identificacion': forms.Select(attrs={'class': 'form-control'}),
            'identificacion': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Número de identificación'
            }),
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control',
                                                    'onkeyup': "javascript:this.value=this.value.toUpperCase();",}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control',
                                                     'onkeyup': "javascript:this.value=this.value.toUpperCase();",}),
            'primer_apellido': forms.TextInput(attrs={'class': 'form-control',
                                                      'onkeyup': "javascript:this.value=this.value.toUpperCase();",}),
            'segundo_apellido': forms.TextInput(attrs={'class': 'form-control',
                                                       'onkeyup': "javascript:this.value=this.value.toUpperCase();",}),
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type': 'date'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'altura': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class DatosPersonaFilterForm(forms.ModelForm):
    class Meta:
        model = DatosPersona
        fields = ['es_estudiante', 'peso', 'altura', 'clasificacion']
        widgets = {
            'es_estudiante': forms.CheckboxInput(attrs={'class': 'form-control'}),
            'peso': forms.NumberInput(attrs={'class': 'form-control'}),
            'altura': forms.NumberInput(attrs={'class': 'form-control'}),
            'clasificacion': forms.Select(attrs={'class': 'form-control'}),
        }
