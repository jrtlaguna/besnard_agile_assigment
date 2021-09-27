import pytest

from values_principles.models import Value, Principle


@pytest.mark.django_db
class TestFilmViews:
    def test_create_value(self, client):
        assert Value.objects.count() == 0
        response = client.post(
            "/api/v1/values_principles/values/",
            {
                "title": "Test Value Title",
                "content": "Test Value Content",
            },
        )

        assert response.status_code == 201, response.data
        assert response.json() == {
            "id": response.json()["id"],
            "title": "Test Value Title",
            "content": "Test Value Content",
        }

    def test_list_value(self, client):
        assert Value.objects.count() == 0
        value = Value.objects.create(
            title="Test Value Title",
            content="Test Value Content",
        )

        response = client.get("/api/v1/values_principles/values/")

        assert response.status_code == 200
        assert response.json() == [
            {
                "id": value.id,
                "title": "Test Value Title",
                "content": "Test Value Content",
            }
        ]

    def test_get_value_detail(self, client):
        assert Value.objects.count() == 0
        value = Value.objects.create(
            title="Test Value Title",
            content="Test Value Content",
        )
        response = client.get(f"/api/v1/values_principles/values/{value.id}/")

        assert response.status_code == 200
        assert response.json() == {
            "id": value.id,
            "title": "Test Value Title",
            "content": "Test Value Content",
        }

    def test_patch_value(self, client):
        assert Value.objects.count() == 0
        value = Value.objects.create(
            title="Test Value Title",
            content="Test Value Content",
        )
        response = client.patch(
            f"/api/v1/values_principles/values/{value.id}/",
            {"content": "New patched Value Content"},
            content_type="application/json",
        )

        assert response.status_code == 200
        assert response.json() == {
            "id": value.id,
            "title": "Test Value Title",
            "content": "New patched Value Content",
        }

    def test_delete_value(self, client):
        assert Value.objects.count() == 0
        value = Value.objects.create(
            title="Test Value Title",
            content="Test Value Content",
        )

        response = client.delete(
            f"/api/v1/values_principles/values/{value.id}/",
        )
        assert response.status_code == 204

        response = client.get(
            f"/api/v1/values_principles/values/{value.id}/",
        )

        assert response.status_code == 404


@pytest.mark.django_db
class TestFilmPrinciples:
    def test_create_principle(self, client):
        assert Principle.objects.count() == 0
        response = client.post(
            "/api/v1/values_principles/principles/",
            {
                "title": "Test Principle Title",
                "content": "Test Principle Content",
            },
        )
        assert response.status_code == 201, response.data

    def test_list_principle(self, client):
        assert Principle.objects.count() == 0
        principle = Principle.objects.create(
            title="Test Principle Title",
            content="Test Principle Content",
        )

        response = client.get("/api/v1/values_principles/principles/")

        assert response.status_code == 200
        assert response.json() == [
            {
                "id": principle.id,
                "title": "Test Principle Title",
                "content": "Test Principle Content",
            }
        ]

    def test_get_principle_detail(self, client):
        assert Principle.objects.count() == 0
        principle = Principle.objects.create(
            title="Test Principle Title",
            content="Test Principle Content",
        )
        response = client.get(f"/api/v1/values_principles/principles/{principle.id}/")

        assert response.status_code == 200
        assert response.json() == {
            "id": principle.id,
            "title": "Test Principle Title",
            "content": "Test Principle Content",
        }

    def test_patch_principle(self, client):
        assert Principle.objects.count() == 0
        principle = Principle.objects.create(
            title="Test Principle Title",
            content="Test Principle Content",
        )
        response = client.patch(
            f"/api/v1/values_principles/principles/{principle.id}/",
            {"content": "New patched Principle Content"},
            content_type="application/json",
        )

        assert response.status_code == 200
        assert response.json() == {
            "id": principle.id,
            "title": "Test Principle Title",
            "content": "New patched Principle Content",
        }

    def test_delete_principle(self, client):
        assert Principle.objects.count() == 0
        principle = Principle.objects.create(
            title="Test Principle Title",
            content="Test Principle Content",
        )

        response = client.delete(
            f"/api/v1/values_principles/principles/{principle.id}/",
        )
        assert response.status_code == 204

        response = client.get(
            f"/api/v1/values_principles/principles/{principle.id}/",
        )

        assert response.status_code == 404
