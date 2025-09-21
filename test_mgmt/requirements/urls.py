from django.urls import include, path
from rest_framework import routers

from .apiviews import browse_requirements_category
from .views import RequirementsAttachmentViewSet, RequirementsTagViewSet, RequirementsFeatureCategoryViewSet, RequirementsFeatureViewSet, RequirementsUseCaseCategoryViewSet, \
    RequirementsUseCaseViewSet, RequirementCategoryViewSet, RequirementViewSet

router = routers.DefaultRouter()

router.register(r'attachments', RequirementsAttachmentViewSet)
router.register(r'tags', RequirementsTagViewSet)
router.register(r'feature_categories', RequirementsFeatureCategoryViewSet)
router.register(r'features', RequirementsFeatureViewSet)

router.register(r'use_case_categories', RequirementsUseCaseCategoryViewSet)
router.register(r'use_cases', RequirementsUseCaseViewSet)
router.register(r'requirement_categories', RequirementCategoryViewSet)
router.register(r'requirements', RequirementViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/browse_requirements_category', browse_requirements_category),
]
