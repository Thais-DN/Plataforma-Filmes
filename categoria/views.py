from rest_framework import viewsets
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