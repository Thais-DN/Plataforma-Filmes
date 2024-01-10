from django.db import models
from movie.models import Filme

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to='movie_images/')
    filmes = models.ManyToManyField(Filme)

    def __str__(self):
        return self.nome
    
class SubCategoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to='movie_images/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    filmes = models.ManyToManyField(Filme)

    def __str__(self):
        return self.nome