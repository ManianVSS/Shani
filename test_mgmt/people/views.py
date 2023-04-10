from rest_framework import permissions
from rest_framework import viewsets

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    exact_fields_filter_lookups, compare_fields_filter_lookups, date_fields_filter_lookups
from .models import Engineer, SiteHoliday, Leave, \
    EngineerOrgGroupParticipation, Topic, TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Site, \
    Attachment
from .serializers import EngineerSerializer, \
    SiteHolidaySerializer, \
    LeaveSerializer, EngineerOrgGroupParticipationSerializer, TopicSerializer, TopicEngineerAssignmentSerializer, \
    EngineerOrgGroupParticipationHistorySerializer, SiteSerializer, AttachmentSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
    }


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,

    }


class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'employee_id', 'name', 'auth_user', 'role', 'site', 'org_group', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'employee_id': exact_fields_filter_lookups,
        'name': exact_fields_filter_lookups,
        'auth_user': id_fields_filter_lookups,
        'role': exact_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'site': id_fields_filter_lookups,
        'auth_user__username': exact_fields_filter_lookups,
    }


class EngineerOrgGroupParticipationViewSet(viewsets.ModelViewSet):
    queryset = EngineerOrgGroupParticipation.objects.all()
    serializer_class = EngineerOrgGroupParticipationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'engineer', 'org_group', 'published', 'role', 'capacity', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'role': string_fields_filter_lookups,
        'capacity': compare_fields_filter_lookups,
    }


class SiteHolidayViewSet(viewsets.ModelViewSet):
    queryset = SiteHoliday.objects.all()
    serializer_class = SiteHolidaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'date', 'site', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'date': date_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'site': id_fields_filter_lookups,
    }


class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [permissions.DjangoObjectPermissions]
    search_fields = default_search_fields
    ordering_fields = ['id', 'engineer', 'start_date', 'end_date', 'status', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
    }


class EngineerOrgGroupParticipationHistoryViewSet(viewsets.ModelViewSet):
    queryset = EngineerOrgGroupParticipationHistory.objects.all()
    serializer_class = EngineerOrgGroupParticipationHistorySerializer
    permission_classes = [permissions.DjangoObjectPermissions]
    search_fields = default_search_fields
    ordering_fields = ['id', 'date', 'engineer', 'org_group', 'published', 'expected_capacity', 'capacity', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'date': date_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'expected_capacity': compare_fields_filter_lookups,
        'capacity': compare_fields_filter_lookups,
    }


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'description', 'parent_topic', 'org_group', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'parent_topic': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
    }


class TopicEngineerAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TopicEngineerAssignment.objects.all()
    serializer_class = TopicEngineerAssignmentSerializer
    permission_classes = [permissions.DjangoObjectPermissions]
    search_fields = default_search_fields
    ordering_fields = ['id', 'topic', 'engineer', 'status', 'rating', 'start_date', 'end_date', 'org_group',
                       'published', ]
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
    }
