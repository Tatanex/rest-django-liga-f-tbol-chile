# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from PrimeraA.serializers import EquipoSerializer
from PrimeraA.models import Equipo


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer




class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def equipo_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        equipos = Equipo.objects.all()
        serializer = EquipoSerializer(equipos, many=True)
        clubs =  JSONResponse(serializer.data)
        # return render (request, 'index.html', {'clubs': clubs})
        return render (request, 'index.html', {'clubs': equipos})


    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EquipoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def equipo_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        equipo = Equipo.objects.get(pk=pk)
    except Equipo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EquipoSerializer(equipo)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EquipoSerializer(equipo, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        equipo.delete()
        return HttpResponse(status=204)