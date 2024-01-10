from .models import Filme
from rest_framework import viewsets, generics
from .serializers import FilmeSerializers
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
import logging

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class GetFilme(generics.ListAPIView):
    serializer_class = FilmeSerializers
    
    def get_queryset(self):
        print(self.request)
        id_filme=self.kwargs['id_filme']
        print(id_filme)
        return Filme.objects.filter(pk=id_filme)
