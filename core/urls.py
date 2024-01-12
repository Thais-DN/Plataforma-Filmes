from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from movie.views import FilmeViewSet, GetFilme, GetFilmesGrupo, GrupoViewSet
from categoria.views import CategoriaViewSet, SubCategoriaViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'filmes', FilmeViewSet)
router.register(r'grupo', GrupoViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'sub_categorias', SubCategoriaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    re_path('^api/filme/(?P<id_filme>.+)/$', GetFilme.as_view()),
    re_path('^api/grupo/(?P<id_grupo>.+)/filmes/$', GetFilmesGrupo.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

