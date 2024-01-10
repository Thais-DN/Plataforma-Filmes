from rest_framework import serializers
from .models import Categoria, SubCategoria

class CategoriaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Categoria
        fields = ["id","nome", "imagem"]
        
class SubCategoriaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = SubCategoria
        fields = ["id","nome", "imagem", "categoria"]
