from django.shortcuts import render

from rest_framework import permissions, viewsets
from .serializers import GeneroSerializer, FilmeSerializer, SessaoSerializer
from .models import User, Genero, Filme, Sessao


class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    
class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    
class SessaoViewSet(viewsets.ModelViewSet):
    queryset = Sessao.objects.all()
    serializer_class = SessaoSerializer