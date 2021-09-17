from django.urls import path, include

from rest_framework.routers import DefaultRouter

from values_principles.api.v1 import viewsets

router = DefaultRouter()
router.register(
    "values",
    viewsets.ValueViewSet,
    basename="values",
)
router.register(
    "principles",
    viewsets.PrincipleViewSet,
    basename="principles",
)

urlpatterns = [path(r"", include(router.urls))]
