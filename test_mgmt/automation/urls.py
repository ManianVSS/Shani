from django.urls import include, path
from rest_framework import routers

from .views import AttachmentViewSet, TagViewSet, StepViewSet, PropertiesViewSet, MockAPIViewSet, \
    MockAPIRoutingViewSet, ApplicationUnderTestViewSet, ApplicationPageViewSet, ElementViewSet

router = routers.DefaultRouter()

# TODO: Fix urls in browsable UI for viewsets resolved with same view names
router.register(r'attachments', AttachmentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'steps', StepViewSet)
router.register(r'properties', PropertiesViewSet)

router.register(r'mockapi', MockAPIViewSet)
router.register(r'mockapi_call', MockAPIRoutingViewSet, basename='mock api call', )

router.register(r'applications_under_test', ApplicationUnderTestViewSet)
router.register(r'apppages', ApplicationPageViewSet)
router.register(r'elements', ElementViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
