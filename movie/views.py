from .models import Filme, Grupo
from rest_framework import viewsets, generics
from .serializers import FilmeSerializers, GrupoSerializers
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class GetFilme(generics.ListAPIView):
    serializer_class = FilmeSerializers
    
    def get_queryset(self):
        id_filme=self.kwargs['id_filme']
        return Filme.objects.filter(pk=id_filme)
    
class GetFilmesGrupo(generics.ListAPIView):
    serializer_class = FilmeSerializers
    
    def get_queryset(self):
        id_grupo=self.kwargs['id_grupo']
        grupo=Grupo.objects.get(pk=id_grupo)
        return Filme.objects.filter(grupo=grupo)
