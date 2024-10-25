from django.urls import include, path
from rest_framework import routers

from .apiviews import get_org_capacity_for_time_range, get_engineer_capacity_for_time_range
from .views import EngineerViewSet, SiteHolidayViewSet, LeaveViewSet, EngineerOrgGroupParticipationViewSet, \
    TopicViewSet, TopicEngineerAssignmentViewSet, EngineerOrgGroupParticipationHistoryViewSet, AttachmentViewSet, \
    CreditViewSet, ScaleViewSet, ReasonViewSet, EngineerSkillsViewSet

router = routers.DefaultRouter()
router.register(r'attachments', AttachmentViewSet)

router.register(r'engineers', EngineerViewSet)
router.register(r'engineer_org_group_participation', EngineerOrgGroupParticipationViewSet)
router.register(r'site_holidays', SiteHolidayViewSet)
router.register(r'leaves', LeaveViewSet)
router.register(r'engineer_org_group_participation_history', EngineerOrgGroupParticipationHistoryViewSet)
router.register(r'engineer_skills', EngineerSkillsViewSet)

router.register(r'topics', TopicViewSet)
router.register(r'topic_engineer_assignments', TopicEngineerAssignmentViewSet)

router.register(r'scales', ScaleViewSet)
router.register(r'reasons', ReasonViewSet)
router.register(r'credits', CreditViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),

    path('api/capacity_view', get_org_capacity_for_time_range),
    path('api/engineer_capacity_view', get_engineer_capacity_for_time_range),
]
