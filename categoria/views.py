from rest_framework import viewsets, generics
from .serializers import CategoriaSerializers, SubCategoriaSerializers
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .models import Categoria, SubCategoria

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class SubCategoriaViewSet(viewsets.ModelViewSet):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class GetCategoria(generics.ListAPIView):
    serializer_class = SubCategoriaSerializers
    
    def get_queryset(self):
        id_categoria=self.kwargs['id_categoria']
        return SubCategoria.objects.filter(categoria=id_categoria)