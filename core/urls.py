from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from movie.views import FilmeViewSet, GetFilme

router = routers.DefaultRouter()
router.register(r'filmes', FilmeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    re_path('^filme/(?P<id_filme>.+)/$', GetFilme.as_view())
]

