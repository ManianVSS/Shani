from rest_framework import permissions

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    exact_fields_filter_lookups, compare_fields_filter_lookups, date_fields_filter_lookups, \
    ShaniOrgGroupObjectLevelPermission, ShaniOrgGroupViewSet, datetime_fields_filter_lookups
from .models import Engineer, SiteHoliday, Leave, \
    EngineerOrgGroupParticipation, Topic, TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Site, \
    Attachment, Credit, Scale, Reason, EngineerSkills
from .serializers import EngineerSerializer, \
    SiteHolidaySerializer, \
    LeaveSerializer, EngineerOrgGroupParticipationSerializer, TopicSerializer, TopicEngineerAssignmentSerializer, \
    EngineerOrgGroupParticipationHistorySerializer, SiteSerializer, AttachmentSerializer, CreditSerializer, \
    ScaleSerializer, ReasonSerializer, EngineerSkillsSerializer


class AttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class SiteViewSet(ShaniOrgGroupViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,

    }


class EngineerViewSet(ShaniOrgGroupViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'employee_id', 'name', 'auth_user', 'role', 'site', 'points', 'org_group', 'created_at',
                       'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'employee_id': exact_fields_filter_lookups,
        'name': exact_fields_filter_lookups,
        'auth_user': id_fields_filter_lookups,
        'role': exact_fields_filter_lookups,
        'site': id_fields_filter_lookups,
        'points': compare_fields_filter_lookups,
        'auth_user__username': exact_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class EngineerOrgGroupParticipationViewSet(ShaniOrgGroupViewSet):
    queryset = EngineerOrgGroupParticipation.objects.all()
    serializer_class = EngineerOrgGroupParticipationSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'engineer', 'org_group', 'role', 'capacity', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'role': string_fields_filter_lookups,
        'capacity': compare_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class SiteHolidayViewSet(ShaniOrgGroupViewSet):
    queryset = SiteHoliday.objects.all()
    serializer_class = SiteHolidaySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'date', 'site', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'date': date_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'site': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class LeaveViewSet(ShaniOrgGroupViewSet):
    queryset = Leave.objects.filter(published=True)
    serializer_class = LeaveSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoObjectPermissions]
    search_fields = default_search_fields
    ordering_fields = ['id', 'engineer', 'start_date', 'end_date', 'status', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class EngineerOrgGroupParticipationHistoryViewSet(ShaniOrgGroupViewSet):
    queryset = EngineerOrgGroupParticipationHistory.objects.filter(published=True)
    serializer_class = EngineerOrgGroupParticipationHistorySerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoObjectPermissions]
    search_fields = default_search_fields
    ordering_fields = ['id', 'date', 'engineer', 'org_group', 'created_at', 'updated_at', 'published',
                       'expected_capacity', 'capacity', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'date': date_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'expected_capacity': compare_fields_filter_lookups,
        'capacity': compare_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,

    }


class TopicViewSet(ShaniOrgGroupViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'description', 'parent_topic', 'org_group', 'created_at', 'updated_at',
                       'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'parent_topic': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class TopicEngineerAssignmentViewSet(ShaniOrgGroupViewSet):
    queryset = TopicEngineerAssignment.objects.filter(published=True)
    serializer_class = TopicEngineerAssignmentSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.DjangoObjectPermissions]
    search_fields = default_search_fields
    ordering_fields = ['id', 'topic', 'engineer', 'status', 'rating', 'start_date', 'end_date', 'org_group',
                       'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'topic': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'rating': compare_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class ScaleViewSet(ShaniOrgGroupViewSet):
    queryset = Scale.objects.all()
    serializer_class = ScaleSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class ReasonViewSet(ShaniOrgGroupViewSet):
    queryset = Reason.objects.all()
    serializer_class = ReasonSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'org_group', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class CreditViewSet(ShaniOrgGroupViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = ['time', 'credited_user', 'scale', 'reason', 'creditor']
    ordering_fields = ['id', 'time', 'credited_user', 'scale', 'reason', 'creditor', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'time': date_fields_filter_lookups,
        'credited_user': id_fields_filter_lookups,
        'credits': compare_fields_filter_lookups,
        'scale': id_fields_filter_lookups,
        'reason': id_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'creditor': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class EngineerSkillsViewSet(ShaniOrgGroupViewSet):
    queryset = EngineerSkills.objects.all()
    serializer_class = EngineerSkillsSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'engineer', 'skill', 'experience', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'skill': string_fields_filter_lookups,
        'experience': compare_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }
