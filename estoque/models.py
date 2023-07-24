from django.db import models

class Materiais(models.Model):
    quantidade = models.IntegerField()
    descricao = models.TextField()
    data = models.DateField()
    
    def __str__(self):
        return self.descricao
