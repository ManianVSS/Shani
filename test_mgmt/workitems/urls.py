from django.urls import include, path
from rest_framework import routers

from .views import AttachmentViewSet, TagViewSet, ReleaseViewSet, EpicViewSet, FeatureViewSet, SprintViewSet, \
    StoryViewSet, FeedbackViewSet

router = routers.DefaultRouter()

router.register(r'attachments', AttachmentViewSet)
router.register(r'tags', TagViewSet)
router.register(r'releases', ReleaseViewSet)
router.register(r'epics', EpicViewSet)
router.register(r'features', FeatureViewSet)
router.register(r'sprints', SprintViewSet)
router.register(r'stories', StoryViewSet)
router.register(r'feedbacks', FeedbackViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
