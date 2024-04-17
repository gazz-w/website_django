from django.db import models


class Servico(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    especialidade = models.CharField(
        max_length=100, null=False, blank=False, default='default')
    profissionais = models.ManyToManyField(
        'Profissional', related_name='servicos')

    def __str__(self):
        return f"Serviço [Nome={self.nome}, Especialidade={self.especialidade}]"


class Profissional(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    especialidade = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Profissional [Nome={self.nome}, Especialidade={self.especialidade}]"


class Paciente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True)
    cpf = models.IntegerField(unique=True)

    def __str__(self):
        return f"Paciente [Nome={self.nome}]"

# Create your models here.
