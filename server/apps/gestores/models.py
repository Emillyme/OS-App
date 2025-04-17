from django.db import models


class Gestor(models.Model):
    sn_gest = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} - {self.cargo}"