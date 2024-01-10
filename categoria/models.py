from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to='movie_images/')

    def __str__(self):
        return self.nome
    
class SubCategoria(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    imagem = models.ImageField(upload_to='movie_images/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome