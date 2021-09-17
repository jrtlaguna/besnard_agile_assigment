import factory

from values_principles.models import Value, Principle


class ValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Value

    title = "Test Title"
    content = "Test Content"


class PrincipleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Principle

    title = "Test Title"
    content = "Test Content"
