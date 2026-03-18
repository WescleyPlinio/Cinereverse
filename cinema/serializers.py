from rest_framework import serializers
from .models import User, Genero, Filme, Sessao

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['nome']

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = ['titulo', 'sinopse', 'genero', 'ano_lancamento', 'duracao_em_min', 'faixa_etaria']

class SessaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessao
        fields = ['filme', 'quantidade_cadeiras']