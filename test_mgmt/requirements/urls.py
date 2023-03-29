from django.urls import include, path
from rest_framework import routers

from automation.views import StepViewSet, AttachmentViewSet, ProductFeatureViewSet

router = routers.DefaultRouter()

router.register(r'attachments', AttachmentViewSet)
router.register(r'features', ProductFeatureViewSet)
router.register(r'steps', StepViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
