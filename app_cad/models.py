from django.db import models

class cliente(models.Model):
    nome_completo = models.CharField(max_length=256)
    endereco = models.CharField(max_length=256)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=256)
    data_criacao = models.DateField(null=True)
    

    def __str__(self) -> str:
        return self.nome_completo