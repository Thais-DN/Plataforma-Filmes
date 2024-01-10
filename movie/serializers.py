from rest_framework import serializers
from .models import Filme
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

class FilmeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Filme
        fields = ["nome", "ano", "duracao", "descricao", "imagem"]
        permission_classes = [DjangoModelPermissionsOrAnonReadOnly]