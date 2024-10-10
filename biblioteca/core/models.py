from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

class Autor(models.Model):
    nome = models.CharField(max_length=100)

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado_em = models.DateField()