from django.urls import include, path
from rest_framework import routers

from .views import AttachmentViewSet, TagViewSet, FeatureCategoryViewSet, FeatureViewSet

router = routers.DefaultRouter()

router.register(r'attachments', AttachmentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'featurecategories', FeatureCategoryViewSet)
router.register(r'features', FeatureViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
