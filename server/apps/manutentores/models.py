from django.db import models
from apps.areas.models import Area
from apps.gestores.models import Gestor

class Manutentor(models.Model):
    sn_manu = models.CharField(max_length=20)
    nome_manu = models.CharField(max_length=100)
    email = models.EmailField()
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)
    gestor = models.ForeignKey(Gestor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome