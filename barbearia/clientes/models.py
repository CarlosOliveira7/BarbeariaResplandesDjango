from django.db import models

# Create your models here.
class Cliente(models.Model): 
    nome = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    email = models.EmailField(max_length=45)

    def __str__(self):
        return self.nome