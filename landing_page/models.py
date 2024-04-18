from django.db import models
from django.utils import timezone


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


class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[(
        'AGENDADO', 'Agendado'), ('CANCELADO', 'Cancelado')], default='AGENDADO')

    def __str__(self):
        return f"Agendamento para {self.paciente.nome} com {self.profissional.nome} em {self.data_hora.strftime('%d/%m/%Y %H:%M')}"

# Create your models here.
