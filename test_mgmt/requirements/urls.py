from django.urls import include, path
from rest_framework import routers

from .apiviews import browse_requirements_category
from .views import AttachmentViewSet, TagViewSet, FeatureCategoryViewSet, FeatureViewSet, UseCaseViewSet, \
    RequirementCategoryViewSet, RequirementViewSet

router = routers.DefaultRouter()

router.register(r'attachments', AttachmentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'feature_categories', FeatureCategoryViewSet)
router.register(r'features', FeatureViewSet)

router.register(r'use_cases', UseCaseViewSet)
router.register(r'requirement_categories', RequirementCategoryViewSet)
router.register(r'requirements', RequirementViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/browse_requirements_category', browse_requirements_category),
]
