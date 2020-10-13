from django.db import models

class Departamento(models.Model):
    nome = models.CharField(max_length=70)

    def __self__(self):
        return self.nome
