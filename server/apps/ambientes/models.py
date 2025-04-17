from django.db import models

class Ambiente(models.Model):
    sig = models.CharField(max_length=20, unique=True)
    descricao = models.CharField(max_length=100)
    sn_resp = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=100) #(resp)onsavel tem que ser cadastrado

    def __str__(self):
        return self.descricao