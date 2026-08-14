from django.urls import include, path
from rest_framework import routers

from .views import SchedulerAttachmentViewSet, SchedulerTagViewSet, ResourceTypeViewSet, ResourceSetViewSet, ResourceSetComponentViewSet, \
    RequestViewSet, ResourceViewSet

router = routers.DefaultRouter()

router.register(r'attachments', SchedulerAttachmentViewSet)
router.register(r'tags', SchedulerTagViewSet)
router.register(r'resource_types', ResourceTypeViewSet)
router.register(r'resource_sets', ResourceSetViewSet)
router.register(r'resource_set_components', ResourceSetComponentViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'resources', ResourceViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
