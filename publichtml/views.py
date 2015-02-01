from django.shortcuts import render, redirect, render_to_response
from publichtml.forms import Personaform
from publichtml.forms import Telefonoform
from publichtml.models import Persona, Variostelefonos
from django.http.response import HttpResponseRedirect
from django.template.context import RequestContext
from django.views.generic.edit import UpdateView
from django.shortcuts import render, redirect, get_object_or_404

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
   
def listartelefonos(request,idpersona):
    conseguirpersona = Persona.objects.filter(id = idpersona ).first()
    telefonossalvados = Variostelefonos.objects.filter(persona=conseguirpersona)      
    return render_to_response('telefono.html',{"telefonodb":telefonossalvados, "personadb":conseguirpersona})

def agregartelefonos(request,idpersona):
    conseguirpersona = Persona.objects.filter(id = idpersona ).first()
    form = Telefonoform()
    if request.method=="POST":
        #telefonopersona = Persona.objects.get(id=idpersona)
        form = Telefonoform(request.POST or None)
        if form.is_valid():
            telefono = form.save(commit=False)
            telefono.persona = conseguirpersona
            telefono.save()
            #return HttpResponseRedirect("publichtml.views.listartelefonos")  
            return redirect("publichtml.views.listartelefonos",idpersona=idpersona)       
    return render_to_response('agregar-telefono.html',{ "telefonodb":form, "personadb":conseguirpersona})

def borrartelefono(request, idtelefono):
    conseguirtelefonoborrar = Variostelefonos.objects.filter(id = idtelefono ).first()
    persona = conseguirtelefonoborrar.persona
    conseguirtelefonoborrar.delete()
    return redirect ("publichtml.views.listartelefonos", idpersona=persona.id)

#def editartelefono(request,idtelefono):
   # telefonossalvados = Variostelefonos.objects.filter(id=idtelefono)
    #return render_to_response('ensenartelefonos.html',{"telefonodb":telefonossalvados},context_instance=RequestContext(request),)
    
def editartelefono(request, idtelefono, template_name='ensenartelefonos.html'):
    salvado= get_object_or_404(Variostelefonos, id=idtelefono)
    persona = salvado.persona
    form = Telefonoform(request.POST or None, instance=salvado)
    if form.is_valid():
        form.save()
        return redirect('publichtml.views.listartelefonos', idpersona=persona.id)
    return render(request, template_name, {'form':form})
    
        
                
        