from rest_framework.serializers import ModelSerializer

from values_principles.models import Principle, Value


class PrincipleSerializer(ModelSerializer):
    class Meta:
        model = Principle
        fields = [
            "id",
            "title",
            "content",
        ]


class ValueSerializer(ModelSerializer):
    class Meta:
        model = Value
        fields = [
            "id",
            "title",
            "content",
        ]
