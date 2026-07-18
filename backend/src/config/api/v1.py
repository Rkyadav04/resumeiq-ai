from django.urls import include, path

urlpatterns = [
    path("health/", include("modules.health.urls")),
]