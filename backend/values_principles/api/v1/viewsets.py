from rest_framework.viewsets import ModelViewSet

from values_principles.models import Principle, Value
from values_principles.api.v1.serializers import PrincipleSerializer, ValueSerializer


class PrincipleViewSet(ModelViewSet):
    queryset = Principle.objects.all()
    serializer_class = PrincipleSerializer


class ValueViewSet(ModelViewSet):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
