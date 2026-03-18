from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Genero(models.Model):
    nome = models.CharField(max_length=120)

class Filme(models.Model):

    FAIXAS_ETARIAS_CHOICES = [
        ("Livre", "Livre"),
        ("10 anos", "10 anos"),
        ("12 anos", "12 anos"),
        ("14 anos", "14 anos"),
        ("16 anos", "16 anos"),
        ("+18", "+18"),
    ]

    titulo = models.CharField(max_length=255)
    sinopse = models.CharField(max_length=1255)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    ano_lancamento = models.DateField()
    duracao_em_min = models.IntegerField()
    faixa_etaria = models.CharField(max_length=50, choices = FAIXAS_ETARIAS_CHOICES)
    
class Sessao(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    quantidade_cadeiras = models.IntegerField(default=120)
