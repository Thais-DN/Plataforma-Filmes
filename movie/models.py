from django.db import models
from categoria.models import Categoria, SubCategoria

class Grupo(models.Model):
        nome = models.CharField(max_length=100, null=False, blank=False)
        imagem = models.ImageField(upload_to='group_images/')
        categoria = models.ManyToManyField(Categoria, related_name='categoria')
        subCategoria = models.ManyToManyField(SubCategoria, related_name='subcategoria')

        def __str__(self):
          return self.nome

class Filme(models.Model):
    escolhas = [
      ("não visto", "não visto"),
      ("visto", "visto"),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    ano = models.CharField(max_length=4, null=False, blank=False)
    duracao = models.CharField(max_length=15, null=False, blank=False)
    descricao = models.CharField(max_length=500, null=False, blank=False)
    imagem = models.ImageField(upload_to='movie_images/')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, null=False, blank=False)
    status = models.CharField(max_length=10, choices=escolhas, null=True, blank=True)

    def __str__(self):
        return self.nome

    
        

    