from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'serverpractica02.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'publichtml.views.home'),
    url(r'^formulario$', 'publichtml.views.personaform'),
    url(r'^lista-personas$', 'publichtml.views.listadepersonas'),
    url(r'^borrarpersona/(?P<idpersona>[0-9]*)$', 'publichtml.views.borrarpersona'),
    url(r'^telefono/(?P<idpersona>[0-9])$', 'publichtml.views.listartelefonos'),
    url(r'^telefono/agregartelefono/(?P<idpersona>[0-9]*)$', 'publichtml.views.agregartelefonos'),
    url(r'^telefono/borrartelefono/(?P<idtelefono>[0-9]*)$', 'publichtml.views.borrartelefono'),
    url(r'^telefono/editartelefono/(?P<idtelefono>[0-9]*)$', 'publichtml.views.editartelefono'),
)
