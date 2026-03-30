from django.db import models
from agendamentos.models import Agendamento

class Financeiro(models.Model):
    TIPO_CHOICES = [
        ('receita', 'Receita'),
        ('despesa', 'Despesa'),
    ]

    tipo = models.CharField(max_length=45, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_lancamento = models.DateTimeField()
    agendamento = models.ForeignKey(
        Agendamento,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='lancamentos'
    )

    def __str__(self):
        return f"{self.tipo} - {self.descricao} (R$ {self.valor})"