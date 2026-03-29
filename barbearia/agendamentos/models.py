from django.db import models
from clientes.models import Cliente
from barbeiros.models import Barbeiro


class Agendamento(models.Model):
    data = models.DateTimeField()

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )

    barbeiro = models.ForeignKey(
        Barbeiro,
        on_delete=models.CASCADE,
        related_name='agendamentos'
    )

    status = models.CharField(
        max_length=45,
        default='pendente'
    )

    def __str__(self):
        return f"{self.cliente} - {self.data}"
    
    