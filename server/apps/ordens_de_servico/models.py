from django.db import models
from apps.ambientes.models import Ambiente
from apps.patrimonios.models import Patrimonio
from apps.manutentores.models import Manutentor
from apps.users.models import User

class OrdemServico(models.Model):
    STATUS_CHOICES = [
        ('iniciada', 'Iniciada'),
        ('pendente', 'Pendente'),
        ('finalizada', 'Finalizada'),
        ('cancelada', 'Cancelada'),
    ]

    PRIORIDADE_CHOICES = [
        ('alta', 'Alta'),
        ('media', 'Média'),
        ('baixa', 'Baixa'),
    ]

    descricao = models.TextField()
    abertura = models.DateTimeField(null=True, blank=True)
    fechamento = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    patrimonio = models.ForeignKey(Patrimonio, on_delete=models.SET_NULL, null=True, blank=True)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    manutentor = models.ForeignKey(Manutentor, on_delete=models.CASCADE)
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='media')
    funcionario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    sn = models.CharField(max_length=20)

    def __str__(self):
        return f"OS {self.id} - {self.status}"