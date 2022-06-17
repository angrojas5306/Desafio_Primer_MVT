from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from .models import Familia

def familia(request):
    familiares = Familia.objects.all()
    contexto = {'familia': familiares}
    plantilla = loader.get_template('familia.html')
    vista_familia = plantilla.render(contexto)
    return HttpResponse(vista_familia)