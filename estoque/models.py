from django.db import models

class Materiais(models.Model):
    quantidade = models.IntegerField()
    descricao = models.TextField()
    data = models.DateField()
    
    def __str__(self):
        return self.descricao


class Revenda(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    

class Saida(models.Model):
    materiais = models.ForeignKey(Materiais, on_delete=models.DO_NOTHING)
    quantidade = models.IntegerField()
    revenda = models.ForeignKey(Revenda, on_delete=models.DO_NOTHING)
    data = models.DateField()
    
    def __str__(self):
        return str(self.materiais)
    