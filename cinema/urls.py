from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"generos", views.GeneroViewSet, basename="generos")
router.register(r"filmes", views.FilmeViewSet, basename="filmes")
router.register(r"sessoes", views.SessaoViewSet, basename="sessoes")

urlpatterns = [
    path("", include(router.urls)),
]
