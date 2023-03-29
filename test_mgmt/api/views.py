from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import viewsets

from .models import UseCase, Requirement, Attachment, UseCaseCategory, OrgGroup, Engineer, SiteHoliday, Leave, \
    EngineerOrgGroupParticipation, Topic, TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Site, Tag

from .serializers import UserSerializer, GroupSerializer, UseCaseSerializer, RequirementSerializer, \
    AttachmentSerializer, UseCaseCategorySerializer, OrgGroupSerializer, EngineerSerializer, SiteHolidaySerializer, \
    LeaveSerializer, EngineerOrgGroupParticipationSerializer, TopicSerializer, TopicEngineerAssignmentSerializer, \
    EngineerOrgGroupParticipationHistorySerializer, SiteSerializer, TagSerializer

exact_fields_filter_lookups = ['exact', ]
id_fields_filter_lookups = ['exact', 'in', ]
string_fields_filter_lookups = ['exact', 'iexact', 'icontains', 'regex', ]
# 'startswith', 'endswith', 'istartswith','iendswith', 'contains',
compare_fields_filter_lookups = ['exact', 'lte', 'lt', 'gt', 'gte', ]
date_fields_filter_lookups = ['exact', 'lte', 'gte', 'range', ]
# date,year, month, day, week, week_day, iso_week, iso_week_day, quarter
datetime_fields_filter_lookups = ['exact', 'lte', 'gte', 'range', ]
# time, hour, minute, second
default_search_fields = ['name', 'summary', 'description', ]
default_ordering = ['id', ]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    search_fields = ['id', 'username', 'first_name', 'last_name', 'email']
    ordering_fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'username': string_fields_filter_lookups,
        'first_name': string_fields_filter_lookups,
        'last_name': string_fields_filter_lookups,
        'email': string_fields_filter_lookups,
        'is_staff': exact_fields_filter_lookups,
        'is_active': exact_fields_filter_lookups,
        'date_joined': date_fields_filter_lookups,
    }


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser]
    search_fields = ['id', 'name', ]
    ordering_fields = ['id', 'name', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'permissions': id_fields_filter_lookups,
    }


# filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)

class OrgGroupViewSet(viewsets.ModelViewSet):
    queryset = OrgGroup.objects.all()
    serializer_class = OrgGroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'auth_group', 'org_group', 'leaders', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'auth_group': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'leaders': id_fields_filter_lookups,
    }


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'employee_id', 'name', 'auth_user', 'role', 'site', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'employee_id': exact_fields_filter_lookups,
        'name': exact_fields_filter_lookups,
        'auth_user': id_fields_filter_lookups,
        'role': exact_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'site': id_fields_filter_lookups,
        'auth_user__username': exact_fields_filter_lookups,
    }


class EngineerOrgGroupParticipationViewSet(viewsets.ModelViewSet):
    queryset = EngineerOrgGroupParticipation.objects.all()
    serializer_class = EngineerOrgGroupParticipationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'engineer', 'org_group', 'role', 'capacity', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'date', 'engineer', 'org_group', 'expected_capacity', 'capacity', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'date': date_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'expected_capacity': compare_fields_filter_lookups,
        'capacity': compare_fields_filter_lookups,
    }


class UseCaseCategoryViewSet(viewsets.ModelViewSet):
    queryset = UseCaseCategory.objects.all()
    serializer_class = UseCaseCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class UseCaseViewSet(viewsets.ModelViewSet):
    queryset = UseCase.objects.all()
    serializer_class = UseCaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'category', 'status', 'weight', 'consumer_score',
                       'serviceability_score', 'test_confidence', 'development_confidence', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,

        'category__name': id_fields_filter_lookups,
        'requirements': id_fields_filter_lookups,
        # 'testcases': id_fields_filter_lookups,

        'weight': compare_fields_filter_lookups,
        'consumer_score': compare_fields_filter_lookups,
        'serviceability_score': compare_fields_filter_lookups,
        'test_confidence': compare_fields_filter_lookups,
        'development_confidence': compare_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'use_cases': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'description', 'parent_topic', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'parent_topic': id_fields_filter_lookups,
    }


class TopicEngineerAssignmentViewSet(viewsets.ModelViewSet):
    queryset = TopicEngineerAssignment.objects.all()
    serializer_class = TopicEngineerAssignmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'topic', 'engineer', 'status', 'rating', 'start_date', 'end_date', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'topic': id_fields_filter_lookups,
        'engineer': id_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'rating': compare_fields_filter_lookups,
        'start_date': date_fields_filter_lookups,
        'end_date': date_fields_filter_lookups,
    }


