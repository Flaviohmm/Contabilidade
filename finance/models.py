from django.db import models

class Ativo(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    circulante = models.BooleanField(default=True) # Indica se é circulante

    def __str__(self):
        return self.nome
    
class Passivo(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    circulante = models.BooleanField(default=True) # Indica se é circulante

    def __str__(self):
        return self.nome
    
class BalancoPatrimonial(models.Model):
    ativos = models.ManyToManyField(Ativo)
    passivos = models.ManyToManyField(Passivo)

    def total_ativos(self):
        return sum(ativo.valor for ativo in self.ativos.all())
    
    def total_passivos(self):
        return sum(passivo.valor for passivo in self.passivos.all())
    
    def patrimonio_liquido(self):
        return self.total_ativos() - self.total_passivos()
