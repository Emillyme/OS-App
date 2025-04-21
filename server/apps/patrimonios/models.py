from django.db import models

class Patrimonio(models.Model):
    ni = models.CharField(max_length=50, null=True, blank=True)
    descricao = models.CharField(max_length=255)
    localizacao = models.CharField(max_length=255)

    def __str__(self):
        return self.descricao