from django.urls import include, path
from rest_framework import routers

from .views import WorkItemsAttachmentViewSet, WorkItemsTagViewSet, ProgramIncrementViewSet, EpicViewSet, WorkItemsFeatureViewSet, SprintViewSet, \
    StoryViewSet, FeedbackViewSet

router = routers.DefaultRouter()

router.register(r'attachments', WorkItemsAttachmentViewSet)
router.register(r'tags', WorkItemsTagViewSet)
router.register(r'program_increments', ProgramIncrementViewSet)
router.register(r'epics', EpicViewSet)
router.register(r'features', WorkItemsFeatureViewSet)
router.register(r'sprints', SprintViewSet)
router.register(r'stories', StoryViewSet)
router.register(r'feedbacks', FeedbackViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
