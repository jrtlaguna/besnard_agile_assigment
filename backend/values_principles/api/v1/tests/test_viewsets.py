from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse

from values_principles.models import Value, Principle
from values_principles.tests.factories import ValueFactory, PrincipleFactory


class ValuesViewSetTestCase(APITestCase):
    def setUp(self):
        self.value = ValueFactory()

    def test_get_value(self):
        res = self.client.get(reverse("values-principles-v1:values-list"))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_value_detail(self):
        res = self.client.get(
            reverse("values-principles-v1:values-detail", kwargs={"pk": self.value.id})
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_value(self):
        data = {
            "title": "Test Value Title",
            "content": "Test Value Content",
        }

        value_count = Value.objects.count()
        res = self.client.post(
            reverse("values-principles-v1:values-list"), data=data, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(value_count + 1, Value.objects.count())

    def test_patch_value(self):
        data = {"content": "New Content"}

        res = self.client.patch(
            reverse("values-principles-v1:values-detail", kwargs={"pk": 1}),
            data=data,
            format="json",
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data.get("content"), "New Content")

    def test_delete_value(self):
        res = self.client.delete(
            reverse("values-principles-v1:values-detail", kwargs={"pk": 1})
        )
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


class PrinciplesViewSetTestCase(APITestCase):
    def setUp(self):
        self.principle = PrincipleFactory()

    def test_get_value(self):
        res = self.client.get(reverse("values-principles-v1:principles-list"))

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_principle_detail(self):
        res = self.client.get(
            reverse(
                "values-principles-v1:principles-detail",
                kwargs={"pk": self.principle.id},
            )
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_principle(self):
        data = {
            "title": "Test Principle Title",
            "content": "Test Principle Content",
        }

        principle_count = Principle.objects.count()
        res = self.client.post(
            reverse("values-principles-v1:principles-list"), data=data, format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(principle_count + 1, Principle.objects.count())

    def test_patch_principle(self):
        data = {"content": "New Content"}

        res = self.client.patch(
            reverse("values-principles-v1:principles-detail", kwargs={"pk": 1}),
            data=data,
            format="json",
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data.get("content"), "New Content")

    def test_delete_principle(self):
        res = self.client.delete(
            reverse("values-principles-v1:principles-detail", kwargs={"pk": 1})
        )
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
