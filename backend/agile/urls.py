from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        r"api/v1/",
        include(
            [
                path(
                    r"values_principles/",
                    include(
                        ("values_principles.api.v1.urls", "values_principles"),
                        namespace="values-principles-v1",
                    ),
                )
            ]
        ),
    ),
]
