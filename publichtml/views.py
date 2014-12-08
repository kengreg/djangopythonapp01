from django.shortcuts import render, redirect
from publichtml.forms import Personaform
from publichtml.models import Persona

# Create your views here.
def home(request):
    return render(request, "index.html")
def personaform(request):
    form = Personaform(request.POST or None)
    if request.method=="POST":
        if form.is_valid():
            persona = form.save()
            return redirect( "publichtml.views.listadepersonas")
    return render(request, "formulario.html",{"formas":form})
def listadepersonas(request):
    personas = Persona.objects.all()
    return render(request, "personas.html",{"listapersonasdb":personas})
def borrarpersona(request, idpersona):
    conseguirpersonaborrar = Persona.objects.filter(id = idpersona ).first()
    conseguirpersonaborrar.delete()
    return redirect ("publichtml.views.listadepersonas")

    
    
    

    