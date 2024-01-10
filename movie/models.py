from django.db import models

class Filme(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    ano = models.CharField(max_length=4, null=False, blank=False)
    duracao = models.CharField(max_length=15, null=False, blank=False)
    descricao = models.CharField(max_length=500, null=True, blank=True)
    imagem = models.ImageField(upload_to='movie_images/')

    def __str__(self):
        return self.nome

    