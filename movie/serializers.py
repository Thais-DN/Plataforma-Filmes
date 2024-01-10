from rest_framework import serializers
from .models import Filme, Grupo

class FilmeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Filme
        fields = ["id","nome", "ano", "duracao", "descricao", "imagem", "grupo", "status"]

class GrupoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Grupo
        fields = ["id","nome", "imagem", "categoria", "subCategoria"]