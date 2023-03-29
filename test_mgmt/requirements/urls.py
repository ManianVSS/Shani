from django.urls import include, path
from rest_framework import routers

from .views import AttachmentViewSet, TagViewSet, FeatureCategoryViewSet, FeatureViewSet, UseCaseViewSet, \
    RequirementViewSet

router = routers.DefaultRouter()

router.register(r'attachments', AttachmentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'featurecategories', FeatureCategoryViewSet)
router.register(r'features', FeatureViewSet)

router.register(r'use_cases', UseCaseViewSet)
router.register(r'requirements', RequirementViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
