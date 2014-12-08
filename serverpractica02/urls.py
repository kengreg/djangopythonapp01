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
    url(r'^borrarpersona/(?P<idpersona>[0-9])$', 'publichtml.views.borrarpersona'),
)
