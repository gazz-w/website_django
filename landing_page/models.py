from django.db import models


class Servico(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return f"Serviço [Nome={self.nome}]"


# Create your models here.
