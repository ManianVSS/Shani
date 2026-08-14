from django.urls import include, path
from rest_framework import routers

from .views import ProgramApplicationTypeViewSet, ProgramApplicationViewSet, ProgramReleaseViewSet, ArtifactTypeViewSet, ArtifactViewSet, \
    DocumentTypeViewSet, DocumentViewSet

router = routers.DefaultRouter()

router.register(r'application_types', ProgramApplicationTypeViewSet)
router.register(r'applications', ProgramApplicationViewSet)
router.register(r'releases', ProgramReleaseViewSet)
router.register(r'artifact_types', ArtifactTypeViewSet)
router.register(r'artifacts', ArtifactViewSet)
router.register(r'document_types', DocumentTypeViewSet)
router.register(r'document', DocumentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
