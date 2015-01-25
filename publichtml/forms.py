from django import forms
#esto lo creas dando click derecho en publichtml carpeta y le das empty
'''
Created on Nov 30, 2014

@author: kengreg
'''
from publichtml.models import Persona
from publichtml.models import Variostelefonos
class Personaform(forms.ModelForm):
    #hacer una def con clean_(nombredel campo) (self)
    def clean_edad(self):
        validadoredad = self.cleaned_data["edad"]
        if validadoredad < 12 or validadoredad > 100:
            raise forms.ValidationError ("Agrege una edad entre entre 12 y 100")
        return validadoredad
    class Meta:
        model = Persona
        fields = ["nombre","apellido","edad","sexo"]

class Telefonoform(forms.ModelForm):
    class Meta:
        model = Variostelefonos
        #fields = ["casa","trabajo","celular","fax","otro"]
        fields = ["casa"]
    