from django.urls import include, path
from rest_framework.routers import DefaultRouter

from endpoints.views import EndpointViewSet
from endpoints.views import MLAlgorithmViewSet
from endpoints.views import MLAlgorithmStatusViewSet
from endpoints.views import MLRequestViewSet
from endpoints.views import home

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet,
                basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("", home)
]
