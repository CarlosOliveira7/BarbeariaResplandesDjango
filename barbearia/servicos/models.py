from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=45)
    preco = models.DecimalField(max_digits=10, decimal_places=2) # Ajustado para suportar decimais

    def __str__(self):
        return self.nome